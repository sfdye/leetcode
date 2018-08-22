class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        N = len(S)
        ans = [N] * N
        p = float("inf")
        for i in itertools.chain(range(N), range(N)[::-1]):
            if S[i] == C:
                p = i
            ans[i] = min(ans[i], abs(p - i))
        return ans
