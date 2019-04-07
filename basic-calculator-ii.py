class Solution:
    def calculate(self, s: str) -> int:
        pre, cur, ans, sign = 0, 0, 0, "+"
        s += "$"
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in "+-*/$":
                if sign == "+":
                    ans += pre
                    pre = cur
                elif sign == "-":
                    ans += pre
                    pre = -cur
                elif sign == "*":
                    pre *= cur
                else:
                    pre = int(pre / cur)
                cur = 0
                sign = c
        return ans + pre
