class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int("{0:{fill}32b}".format(n, fill="0")[::-1], 2)
