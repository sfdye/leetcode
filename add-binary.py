class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j, c = len(a) - 1, len(b) - 1, 0
        ans = ""
        while i >= 0 or j >= 0 or c:
            c += ord(a[i]) - ord("0") if i >= 0 else 0
            c += ord(b[j]) - ord("0") if j >= 0 else 0
            ans = chr((c & 1) + ord("0")) + ans
            i -= 1
            j -= 1
            c >>= 1
        return ans
