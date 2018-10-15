class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        minus = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            multiple, cur = divisor, 1
            while multiple << 1 <= dividend:
                multiple <<= 1
                cur <<= 1
            res += cur
            dividend -= multiple
        if minus:
            res = -res
        return min(max(res, -1 << 31), (1 << 31) - 1)
