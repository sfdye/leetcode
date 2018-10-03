class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                cur_match = i < len(s) and (p[j] == s[i] or p[j] == ".")
                if j + 1 < len(p) and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (cur_match and dp[i + 1][j])
                else:
                    dp[i][j] = cur_match and dp[i + 1][j + 1]
        return dp[0][0]
