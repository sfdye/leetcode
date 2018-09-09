class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(str(n))
        i = len(s) - 1
        while i > 0 and s[i] <= s[i - 1]:
            i -= 1
        if i == 0:
            return -1
        else:
            for j in range(len(s) - 1, -1, -1):
                if s[j] > s[i - 1]:
                    s[i - 1], s[j] = s[j], s[i - 1]
                    break
            s[i:] = s[i:][::-1]
            n = int("".join(s))
            return n if n < (1 << 32 - 1) else -1
