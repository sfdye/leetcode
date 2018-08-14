class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        return [list(x) for x in itertools.permutations(num)]
