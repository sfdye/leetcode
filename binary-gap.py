class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """

        idxs = [idx for idx, c in enumerate(bin(N)[2:]) if c == "1"]
        return max([b - a for a, b in zip(idxs, idxs[1:])] or [0])
