class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo - 1
