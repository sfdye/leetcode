class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        for a, b in ops:
            m = min(m, a)
            n = min(n, b)
        return m * n
