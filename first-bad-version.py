# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if not isBadVersion(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
