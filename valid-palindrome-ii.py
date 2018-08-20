class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N = len(s)
        for i in range(N // 2):
            if s[i] != s[N - 1 - i]:
                j = N - 1 - i
                return s[i + 1 : j + 1] == s[i + 1 : j + 1][::-1] or s[i:j] == s[i:j][::-1]

        return True
