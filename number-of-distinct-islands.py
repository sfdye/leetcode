class Solution:
    def numDistinctIslands(self, grid: "List[List[int]]") -> "int":
        if not grid:
            return 0
        seen = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, d):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r, c) not in seen:
                seen.add((r, c))
                shape.append(d)
                dfs(r + 1, c, 1)
                dfs(r, c + 1, 2)
                dfs(r - 1, c, 3)
                dfs(r, c - 1, 4)
                shape.append(-1)

        shapes = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    shape = []
                    dfs(i, j, 0)
                    if shape:
                        shapes.add(tuple(shape))
        return len(shapes)

