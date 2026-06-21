class Solution:
    # Max-Heap
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time Complexity:  O(n log k)
        # Space Complexity: O(k)
        
        heap = []

        for point in points:
            distance = point[0] ** 2 + point[1] ** 2

            if len(heap) < k:
                heapq.heappush(heap, (-distance, point))
            elif distance < -heap[0][0]:
                heapq.heapreplace(heap, (-distance, point))

        return [point for _, point in heap]


    # Quick Select
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        euclidean = lambda x: x[0]**2 + x[1]**2
        def partition(left, right):
            pivotIdx = right
            pivotDist = euclidean(points[pivotIdx])
            i = left

            for j in range(left, right):
                if euclidean(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[right] = points[right], points[i]
            return i
        
        left, right = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(left, right)
            if pivot < k:
                left = pivot + 1
            else:
                right = pivot - 1
        return points[:k]
