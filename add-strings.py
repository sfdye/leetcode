class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j = len(num1) - 1, len(num2) - 1
        ans, carry = [], 0
        while i >= 0 or j >= 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            ans.append((x + y + carry) % 10)
            carry = (x + y + carry) // 10
            i -= 1
            j -= 1
        if carry > 0:
            ans.append(carry)
        return "".join(map(str, ans[::-1]))

