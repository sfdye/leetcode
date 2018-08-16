class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        s = ""
        for c in S:
            if c in T:
                s += c * T.count(c)
        for c in T:
            if c not in S:
                s += c
        return s
