class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows, cols = len(grid), len(grid[0])
        reach = [[0 for _ in range(cols)] for _ in range(rows)]
        dist = [[0 for _ in range(cols)] for _ in range(rows)]

        def bfs(i, j, cnt):
            queue = collections.deque([(i, j, 0)])
            while queue:
                r, c, step = queue.popleft()
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and reach[nr][nc] == cnt:
                        dist[nr][nc] += step + 1
                        reach[nr][nc] += 1
                        queue.append((nr, nc, step + 1))

        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    bfs(i, j, cnt)
                    cnt += 1

        ans = float("inf")
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and reach[i][j] == cnt:
                    ans = min(ans, dist[i][j])
        return ans if ans < float("inf") else -1

