class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        power_of_five = 1
        sum = 0
        while power_of_five <= n:
            power_of_five *= 5
            sum += n / power_of_five

        return sum
