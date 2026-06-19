class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Time Complexity:  O(n)
        # Space Complexity: O(1)
        
        downOne = 0
        downTwo = 0

        for i in range(2, len(cost) + 1):
            current = min(downOne + cost[i - 1], downTwo + cost[i - 2])

            downTwo = downOne
            downOne = current
        
        return downOne
