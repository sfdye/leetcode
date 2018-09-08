class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(numRows):
            row = [0 for i in range(i + 1)]
            row[0] = row[-1] = 1
            for col in range(1, i):
                row[col] = ans[-1][col - 1] + ans[-1][col]
            ans.append(row)
        return ans
