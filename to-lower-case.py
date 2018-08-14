class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """

        ans = ""

        for c in str:
            if "A" <= c <= "Z":
                ans += chr(ord(c) - (ord("A") - ord("a")))
            else:
                ans += c
        return ans
