class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = (1, -1)[x < 0] * int(str(x).strip("-")[::-1])
        if abs(ans) > 2 ** 31 - 1:
            return 0
        else:
            return ans
