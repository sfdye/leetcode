class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return sum(x % 2 for x in collections.Counter(s).values()) <= 1
