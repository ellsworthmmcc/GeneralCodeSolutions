class Solution:
    def climbStairs(self, n: int) -> int:
        # Time Complexity:  O(n)
        # Space Complexity: O(1)

        one, two = 1, 1

        for _ in range(n-1):
            one, two = one + two, one

        return one
