class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        count = r = c = d = 0
        while count < n * n:
            count += 1
            matrix[r][c] = count
            nr = r + dr[d]
            nc = c + dc[d]
            if nr < 0 or nr == n or nc < 0 or nc == n or matrix[nr][nc] != 0:
                d = (d + 1) % 4
            r += dr[d]
            c += dc[d]
        return matrix
