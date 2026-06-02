class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Time Complexity:  O(n log n)
        # Space Complexity: O(n)

        # Create shallow copy of original nums
        self.k, self.minHeap = k, list(nums)

        heapq.heapify(self.minHeap)

        # Pop elements out until only k largest elements remain
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Time Complexity:  O(log n)
        # Space Complexity: O(1)

        if len(self.minHeap) < self.k:            
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heapq.heapreplace(self.minHeap, val)
        
        return self.minHeap[0]
