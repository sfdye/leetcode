class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(num, path, cur, pre):
            if not num:
                if cur == target:
                    self.ans.append(path)
            else:
                for i in range(1, len(num) + 1):
                    if i == 1 or (i > 1 and num[0] != "0"):
                        val = int(num[:i])
                        dfs(num[i:], path + "+" + str(val), cur + val, val)
                        dfs(num[i:], path + "-" + str(val), cur - val, -val)
                        dfs(num[i:], path + "*" + str(val), cur - pre + pre * val, pre * val)

        self.ans = []
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"):
                dfs(num[i:], num[:i], int(num[:i]), int(num[:i]))
        return self.ans
