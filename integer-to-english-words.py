class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        less_than_20 = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def word(num):
            if num == 0:
                return ""
            elif num < 20:
                return less_than_20[num] + " "
            elif num < 100:
                return tens[num // 10] + " " + word(num % 10)
            else:
                return less_than_20[num // 100] + " Hundred " + word(num % 100)

        ans = ""
        for i in range(len(thousands)):
            if num % 1000 != 0:
                ans = word(num % 1000) + thousands[i] + " " + ans
            num //= 1000
        return ans.strip()
