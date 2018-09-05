class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for x in path.split("/"):
            if x == "" or x == ".":
                continue
            elif x == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        return "/" + "/".join(stack)
