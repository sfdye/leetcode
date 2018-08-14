class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        ans = [""]
        for ch in S:
            if "a" <= ch.lower() <= "z":
                ans = [s + ch.lower() for s in ans] + [s + ch.upper() for s in ans]
            else:
                ans = [s + ch for s in ans]
        return ans
