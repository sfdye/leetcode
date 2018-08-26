counting-bits/class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ones = [0] * (num+1)
        for i in range(1, num+1):
            ones[i] = ones[i & (i-1)] + 1
        return ones
        