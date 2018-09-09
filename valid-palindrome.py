class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join([c for c in s.lower() if c.isalnum()])
        return all(s[i] == s[~i] for i in range(len(s) // 2))
