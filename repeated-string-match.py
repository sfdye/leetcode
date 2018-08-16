class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        k = math.ceil(len(B) / len(A))
        for i in range(2):
            if B in A * (k + i):
                return k + i
        return -1
