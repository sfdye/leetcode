class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1
