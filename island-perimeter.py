class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0

        N = len(grid)
        M = len(grid[0])
        ans = 0
        for i in range(N):
            for j in range(M):
                for k in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    if i + k[0] < 0 or i + k[0] >= N or j + k[1] < 0 or j + k[1] >= M or grid[i + k[0]][j + k[1]] == 0:
                        ans += 1
        return ans
