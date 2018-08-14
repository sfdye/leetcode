class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        subdirs = path.split("/")
        ans = []
        for subdir in subdirs:
            if subdir == "" or subdir == ".":
                continue
            elif subdir == "..":
                if len(ans) > 0:
                    del ans[-1]
            else:
                ans.append(subdir)

        return "/" + "/".join(ans)
