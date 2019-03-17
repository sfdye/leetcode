class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, d):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return
            grid[r][c] = 0
            shape.append(d)
            dfs(r + 1, c, 1)
            dfs(r, c + 1, 2)
            dfs(r - 1, c, 3)
            dfs(r, c - 1, 4)
            shape.append(-1)

        ans = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    shape = []
                    dfs(i, j, 0)
                    ans.add(tuple(shape))
        return len(ans)

