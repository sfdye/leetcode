class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s
        rows = ["" for _ in range(numRows)]
        cur, step = 0, 1
        for c in s:
            rows[cur] += c
            cur += step
            if cur == 0 or cur == numRows - 1:
                step = step * -1
        return "".join(rows)
