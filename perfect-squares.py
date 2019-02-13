class Solution:
    _dp = [0]

    def numSquares(self, n: "int") -> "int":
        while len(self._dp) <= n:
            m = len(self._dp)
            self._dp.append(1 + min(self._dp[m - i * i] for i in range(1, int(m ** 0.5) + 1)))
        return self._dp[n]
