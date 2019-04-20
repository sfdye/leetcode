class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 0, num + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                hi = mid
            else:
                lo = mid + 1
        return (lo - 1) ** 2 == num

