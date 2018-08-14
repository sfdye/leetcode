class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(i, j):
            if i < 0 or i >= N or j < 0 or j >= M or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i, j - 1) + dfs(i - 1, j)

        self.ans = 0
        N, M = len(grid), len(grid[0])

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    self.ans = max(self.ans, dfs(i, j))

        return self.ans
