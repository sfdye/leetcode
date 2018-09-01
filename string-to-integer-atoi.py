class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        sign = -1 if str[0] == "-" else 1
        if str[0] in "+-":
            str = str[1:]
        i = 0
        num = 0
        while i < len(str) and str[i].isdigit():
            num = num * 10 + ord(str[i]) - ord("0")
            i += 1
        num *= sign
        if num < 0:
            return max(-2 ** 31, num)
        else:
            return min(2 ** 31 - 1, num)
