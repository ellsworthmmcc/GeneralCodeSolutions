class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Time Complexity:  O(n * log m)
        # Space Complexity: O(1)
        # n = length of piles, m = max pile size
        left, right = 1, max(piles)
        eatingSpeed = right

        while left <= right:
            mid = left + (right - left) // 2

            totalTime = 0
            for pile in piles:
                totalTime += (pile + mid - 1) // mid
            
            if totalTime <= h:
                eatingSpeed = mid
                right = mid - 1
            else:
                left = mid + 1

        return eatingSpeed
