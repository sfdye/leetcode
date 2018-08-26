import functools


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(functools.reduce(operator.xor, map(ord, s + t)))
