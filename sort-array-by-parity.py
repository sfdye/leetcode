class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        lo, hi = 0, len(A) - 1
        while lo < hi:
            while lo < hi and A[lo] & 1 == 0:
                lo += 1
            while lo < hi and A[hi] & 1 == 1:
                hi -= 1
            if lo < hi:
                A[lo], A[hi] = A[hi], A[lo]
                lo += 1
                hi -= 1
        return A
