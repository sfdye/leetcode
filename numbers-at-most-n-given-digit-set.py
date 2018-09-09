class Solution:
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        s = str(N)
        k = len(s)
        dp = [0] * k + [1]
        for i in range(k - 1, -1, -1):
            for d in D:
                if d < s[i]:
                    dp[i] += len(D) ** (k - i - 1)
                elif d == s[i]:
                    dp[i] += dp[i + 1]

        return dp[0] + sum(len(D) ** i for i in range(1, k))
