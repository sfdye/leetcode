class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        d = {}
        r = {}
        for x, y in zip(s, t):
            if x in d and d[x] != y:
                return False
            if y in d.values() and r[y] != x:
                return False
            if x not in d:
                d[x] = y
                r[y] = x

        return True
