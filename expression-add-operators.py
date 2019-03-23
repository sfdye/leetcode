class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(pos, path, val, pre):
            if pos == len(num):
                if val == target:
                    self.ans.append(path)
            else:
                for i in range(pos, len(num)):
                    if num[pos] == "0" and i != pos:
                        break
                    cur = int(num[pos : i + 1])
                    if pos == 0:
                        dfs(i + 1, path + str(cur), cur, cur)
                    else:
                        dfs(i + 1, path + "+" + str(cur), val + cur, cur)
                        dfs(i + 1, path + "-" + str(cur), val - cur, -cur)
                        dfs(i + 1, path + "*" + str(cur), val - pre + pre * cur, cur * pre)

        self.ans = []
        dfs(0, "", 0, 0)
        return self.ans
