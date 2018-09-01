class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        ans = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        for i in range(len(s)):
            cur = expand(i, i)
            if len(cur) > len(ans):
                ans = cur
            cur = expand(i, i + 1)
            if len(cur) > len(ans):
                ans = cur
        return ans
