class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1.0 / x
            n = abs(n)
        ans, p = 1.0, x
        while n:
            if n & 1:
                ans *= p
            p *= p
            n >>= 1
        return ans
