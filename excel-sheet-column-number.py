class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        power = 1
        for c in s[::-1]:
            ans += power * (ord(c) - ord("A") + 1)
            power *= 26
        return ans
