class Solution:
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans, cur = set(), {0}
        for a in A:
            cur = {a | x for x in cur} | {a}
            ans |= cur
        return len(ans)
