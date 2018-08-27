class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        ans = 0
        for r in range(N):
            for c in range(N):
                cur = grid[r][c]
                if cur:
                    ans += 2
                    for nr, nc in ((r + 1, c), (r, c - 1), (r, c + 1), (r - 1, c)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nei = grid[nr][nc]
                        else:
                            nei = 0
                        ans += max(cur - nei, 0)
        return ans
