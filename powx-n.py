class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        minus = n < 0
        n = abs(n)
        ans, p = 1, x
        while n:
            if n & 1:
                ans *= p
            p *= p
            n >>= 1
        return 1.0 / ans if minus else ans
