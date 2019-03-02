class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(dp[-1][j] + dp[-1][j - 1])
            dp.append(row)
        return dp

