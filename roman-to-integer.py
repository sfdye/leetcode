class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = 0
        for i, c in enumerate(s):
            if i == len(s) - 1 or d[s[i]] >= d[s[i + 1]]:
                n += d[c]
            else:
                n -= d[c]
        return n
