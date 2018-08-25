class Solution:
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        for c in reversed(expression):
            if stack and stack[-1] == "?":
                stack.pop()
                first = stack.pop()
                stack.pop()
                second = stack.pop()
                if c == "T":
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(c)
        return stack[0]
