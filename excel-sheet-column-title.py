class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        ans = ""
        while n:
            m = n % 26
            if m == 0:
                m = 26
                n -= 26
            ans = chr(ord("A") + m - 1) + ans
            n /= 26

        return ans
