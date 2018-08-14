class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        zeros_horizontal = set()
        zeros_vertical = set()
        for row_id, row in enumerate(matrix):
            for col_id, element in enumerate(row):
                if element == 0:
                    zeros_horizontal.add(row_id)
                    zeros_vertical.add(col_id)

        row_count = len(matrix)
        if row_count == 0:
            return
        col_count = len(matrix[0])

        for x in zeros_horizontal:
            for i in range(col_count):
                matrix[x][i] = 0

        for x in zeros_vertical:
            for i in range(row_count):
                matrix[i][x] = 0
