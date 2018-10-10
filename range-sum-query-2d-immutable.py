class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        self.sum_array = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.sum_array[i + 1][j + 1] = (
                    self.sum_array[i + 1][j] + self.sum_array[i][j + 1] + matrix[i][j] - self.sum_array[i][j]
                )

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (
            self.sum_array[row2 + 1][col2 + 1]
            - self.sum_array[row1][col2 + 1]
            - self.sum_array[row2 + 1][col1]
            + self.sum_array[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
