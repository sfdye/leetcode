class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return all(s[i] == s[~i] for i in range(len(s) // 2))
