class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n != 1:
            if n & 1 == 0:
                n >>= 1
            elif n == 3 or n >> 1 & 1 == 0:
                n -= 1
            else:
                n += 1
            res += 1
        return res
