class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return []

        x = 0
        y = 0
        go_up = True
        M = len(matrix)
        N = len(matrix[0])
        count = 0
        total_count = M * N
        ans = []
        while True:
            if go_up:
                i = -1
                j = 1
            else:
                i = 1
                j = -1

            while True:
                ans.append(matrix[x][y])
                count += 1
                if not (0 <= x + i < M and 0 <= y + j < N):
                    break
                x += i
                y += j
            if count == total_count:
                break

            if go_up:
                if y + 1 < N:
                    y += 1
                elif x + 1 < M:
                    x += 1
            else:
                if x + 1 < M:
                    x += 1
                elif y + 1 < N:
                    y += 1
            go_up = not go_up

        return ans
