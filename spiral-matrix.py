class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = d = 0
        rows = len(matrix)
        cols = len(matrix[0])
        ans = []
        for _ in range(rows * cols):
            ans.append(matrix[r][c])
            matrix[r][c] = "#"
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr == rows or nc < 0 or nc == cols or matrix[nr][nc] == "#":
                d = (d + 1) % 4
            r += dr[d]
            c += dc[d]
        return ans

