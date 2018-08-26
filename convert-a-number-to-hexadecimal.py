class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        ans = ""
        d = "0123456789abcdef"
        for _ in range(8):
            ans = d[num & 15] + ans
            num >>= 4
        return ans.lstrip("0")
