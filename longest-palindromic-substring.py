class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        ans = ""

        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1 : j]

        for i in range(len(s)):
            cur = expand(i, i)
            if len(cur) > len(ans):
                ans = cur
            cur = expand(i, i + 1)
            if len(cur) > len(ans):
                ans = cur
        return ans
