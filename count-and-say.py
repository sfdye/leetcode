class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for _ in range(n - 1):
            i = 0
            s += "#"
            next_s = ""
            for j in range(1, len(s)):
                if s[j] != s[j - 1]:
                    next_s += str(j - i) + s[j - 1]
                    i = j
            s = next_s
        return s
