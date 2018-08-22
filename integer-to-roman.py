class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        while num:
            if num > 999:
                ans += "M" * (num // 1000)
                num %= 1000
            elif num > 99:
                d = num // 100
                if 1 <= d < 4:
                    ans += "C" * d
                elif d == 4:
                    ans += "CD"
                elif 4 < d <= 8:
                    ans += "D" + "C" * (d - 5)
                else:
                    ans += "CM"
                num %= 100
            elif num > 9:
                d = num // 10
                if 1 <= d < 4:
                    ans += "X" * d
                elif d == 4:
                    ans += "XL"
                elif 4 < d <= 8:
                    ans += "L" + "X" * (d - 5)
                else:
                    ans += "XC"
                num %= 10
            else:
                d = num
                if 1 <= d < 4:
                    ans += "I" * d
                elif d == 4:
                    ans += "IV"
                elif 4 < d <= 8:
                    ans += "V" + "I" * (d - 5)
                else:
                    ans += "IX"
                num %= 1
        return ans
