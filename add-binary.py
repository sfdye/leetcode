class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        if len(a) < len(b):
            a, b = b, a
        a = list(a)[::-1]
        b = list(b)[::-1]
        sum = 0
        ans = ""
        for i in range(len(a)):
            sum += int(a[i])
            sum += int(b[i]) if i < len(b) else 0
            ans += str(sum % 2)
            sum //= 2  # carry
        if sum:
            ans += str(sum)

        return ans[::-1]
