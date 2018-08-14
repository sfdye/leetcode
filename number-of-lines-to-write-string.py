class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """

        ans = [1, 100]
        for c in S:
            if widths[ord(c) - ord("a")] <= ans[1]:
                ans[1] -= widths[ord(c) - ord("a")]
            else:
                ans[0] += 1
                ans[1] = 100 - widths[ord(c) - ord("a")]
        ans[1] = 100 - ans[1]
        return ans
