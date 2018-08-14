class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        digit = 1
        nine = 9
        while True:
            if n > digit * nine:
                n -= digit * nine
                nine *= 10
                digit += 1
            else:
                break

        num = nine // 9 + (n - 1) // digit
        return int(str(num)[(n - 1) % digit])
