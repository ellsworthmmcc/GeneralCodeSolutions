class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time Complexity:  O(m * n)
        # Space Complexity: O(m * n)
        # m = number of rows, n = number of columns
        if not grid:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(row, col):
            q = deque()
            grid[row][col] = '0'
            q.append((row, col))

            while q:
                row, col = q.popleft()
                for rowDir, colDir in directions:
                    rowNew, colNew = rowDir + row, colDir + col
                    if (
                        rowNew < 0 or colNew < 0 or 
                        rowNew >= ROWS or colNew >= COLS or 
                        grid[rowNew][colNew] == '0'
                    ):
                        continue
                    q.append((rowNew, colNew))
                    grid[rowNew][colNew] = '0'


        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    bfs(row, col)
                    islands += 1

        return islands
