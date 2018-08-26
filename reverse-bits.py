class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for _ in range(32):
            ans <<= 1
            ans |= n & 1
            n >>= 1
        return ans
