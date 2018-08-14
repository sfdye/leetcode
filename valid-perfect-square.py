class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        while x ** 2 > num:
            x = (x + num / x) / 2
        return x ** 2 == num
