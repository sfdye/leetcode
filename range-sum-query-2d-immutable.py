class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                self.sum[i + 1][j + 1] = self.sum[i + 1][j] + self.sum[i][j + 1] + matrix[i][j] - self.sum[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sum[row2 + 1][col2 + 1] - self.sum[row1][col2 + 1] - self.sum[row2 + 1][col1] + self.sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
