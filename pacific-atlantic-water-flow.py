class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []

        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def bfs(reacheable):
            queue = collections.deque(reacheable)
            while queue:
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0
                        or nr >= rows
                        or nc < 0
                        or nc >= cols
                        or (nr, nc) in reacheable
                        or matrix[nr][nc] < matrix[r][c]
                    ):
                        continue
                    queue.append((nr, nc))
                    reacheable.add((nr, nc))

            return reacheable

        rows, cols = len(matrix), len(matrix[0])
        pacific = {(row, 0) for row in range(rows)} | {(0, col) for col in range(cols)}
        atlantic = {(rows - 1, col) for col in range(cols)} | {(row, cols - 1) for row in range(rows)}
        return list(bfs(atlantic) & bfs(pacific))
