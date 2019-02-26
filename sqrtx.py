class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif mid ** 2 > x:
                hi = mid - 1
            else:
                lo = mid + 1

