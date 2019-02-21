class Solution:
    def restoreIpAddresses(self, s: "str") -> "List[str]":
        def dfs(cur, dep, s):
            if dep > 4:
                return
            if dep == 4 and s == "":
                res.add(".".join(cur))
                return

            if s != "":
                dfs(cur + [s[:1]], dep + 1, s[1:])
            if len(s) > 1 and s[0] != "0":
                dfs(cur + [s[:2]], dep + 1, s[2:])
            if len(s) > 2 and s[0] != "0" and 0 <= int(s[:3]) <= 255:
                dfs(cur + [s[:3]], dep + 1, s[3:])

        res = set()

        dfs([], 0, s)

        return list(res)
