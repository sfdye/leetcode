import math


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        for a in range(int(math.sqrt(c / 2) + 1)):
            b = c - a ** 2
            if int(math.sqrt(b)) ** 2 == b:
                return True
        return False
