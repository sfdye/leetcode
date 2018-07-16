class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x <= 1:
            return x

        s = x/2

        while abs(s**2-x)>1e-6:

            s = 0.5*(s+x/s)
            print s

        return int(s)
