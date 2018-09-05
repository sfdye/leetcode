class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 2
        for _ in range(n - 1):
            a, b = b, a + b
        return a
