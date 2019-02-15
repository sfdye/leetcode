class Solution:
    def minAddToMakeValid(self, S: "str") -> "int":
        ans = bal = 0
        for s in S:
            if s == "(":
                bal += 1
            else:
                bal -= 1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal
