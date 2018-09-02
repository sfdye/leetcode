class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def construct(left, right, cur):
            if left + right == n * 2:
                ans.append(cur)
                return
            if left < n:
                construct(left + 1, right, cur + "(")
            if right < left:
                construct(left, right + 1, cur + ")")

        construct(0, 0, "")
        return ans
