class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        minus = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while divisor <= dividend:
            multiple, q = divisor, 1
            while multiple + multiple <= dividend:
                multiple += multiple
                q += q
            dividend -= multiple
            quotient += q
        if minus:
            quotient = -quotient
        return min(max(quotient, -1 << 31), (1 << 31) - 1)
