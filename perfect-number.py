import math


class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 2:
            return False

        divisor_sum = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                divisor_sum += (i + num // i)
            if divisor_sum > num:
                break
        return divisor_sum == num
