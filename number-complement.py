class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = 1
        while mask <= num:
            num ^= mask
            mask <<= 1
        return num
