class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        d = {x: i for i, x in enumerate(B)}
        return [d[x] for x in A]
