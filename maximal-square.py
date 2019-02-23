class Solution:
    def maximalSquare(self, matrix: "List[List[str]]") -> "int":
        rows, cols = len(matrix), len(matrix[0]) if matrix else 0
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        ans = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0
        return ans ** 2
