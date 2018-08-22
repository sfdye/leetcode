class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        d = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i - j not in d:
                    d[i - j] = matrix[i][j]
                else:
                    if d[i - j] != matrix[i][j]:
                        return False
        return True
