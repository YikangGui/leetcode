class Solution:
    def numIslands(self, grid) -> int:
        def dfs(i, j):
            if 0 <= i < m:
                if 0 <= j < n:
                    if grid[i][j] == '1':
                        grid[i][j] = 0
                        dfs(i + 1, j)
                        dfs(i - 1, j)
                        dfs(i, j + 1)
                        dfs(i, j - 1)

        res = 0
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res
