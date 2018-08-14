class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        t = [[0 for y in range(x)] for x in range(1, numRows + 1)]
        t[0][0] = 1

        for i in range(1, numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    t[i][j] = 1
                else:
                    t[i][j] = t[i - 1][j - 1] + t[i - 1][j]
        return t
