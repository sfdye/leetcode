class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = match = 0
        star_pos = -1
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            elif j < len(p) and p[j] == "*":
                star_pos = j
                match = i
                j += 1
            elif star_pos != -1:
                j = star_pos + 1
                match += 1
                i = match
            else:
                return False
        return all(x == "*" for x in p[j:])
