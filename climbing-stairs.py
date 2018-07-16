class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 2
        for i in range(n-1):
            a, b = b, a + b

        return a
