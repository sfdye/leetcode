class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bits = bin(n)[2:]
        return all(bits[i] != bits[i + 1] for i in range(len(bits) - 1))
