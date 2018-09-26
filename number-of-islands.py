class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count = 0
        r, c = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for d in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                dfs(i + d[0], j + d[1])

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count

