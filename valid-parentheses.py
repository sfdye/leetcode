class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack or stack.pop() != pair[c]:
                    return False
        return not stack
