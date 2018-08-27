class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return len({("".join(sorted(s[0::2])), "".join(sorted(s[1::2]))) for s in A})
