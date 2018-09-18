class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for d in num:
            while stack and k and d < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(d)
        return "".join(stack[: len(stack) - k]).lstrip("0") or "0"
