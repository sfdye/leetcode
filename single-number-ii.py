class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        d = {}
        for x in A:
            if not x in d:
                d[x] = 1
            else:
                d[x] += 1
        for k, v in d.items():
            if v != 3:
                return k
