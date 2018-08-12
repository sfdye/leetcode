class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def transform(s):
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                else:
                    if stack:
                        stack.pop()
            return stack

        return transform(S) == transform(T)
