class Solution:
    # Dynamic Programming (Bottom-Up)
    def uniquePaths(self, m: int, n: int) -> int:
        # Time Complexity:  O(m * n)
        # Space Complexity: O(m * n)
        # m = number of rows, n = number of cols

        memo = [[-1] * n for _ in range(m)]
        def dfs(i, j):
            if i == (m - 1) and j == (n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            
            memo[i][j] = dfs(i, j + 1) + dfs(i + 1, j)
            return memo[i][j]
        
        return dfs(0, 0)

class Solution:
    # Dynamic Programming
    def uniquePaths(self, m: int, n: int) -> int:
        # Time Complexity:  O(m * n)
        # Space Complexity: O(n)
        # m = number of rows, n = number of cols
        dp = [1] * n
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[j] += dp[j + 1]

        return dp[0]
