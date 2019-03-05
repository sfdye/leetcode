class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            grid[r][c] = "0"
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    ans += 1
        return ans
