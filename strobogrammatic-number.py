class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """

        for i in range(len(num) // 2 + 1):
            j = len(num) - i - 1
            if not (
                (num[i] == num[j] == "0")
                or (num[i] == num[j] == "1")
                or (num[i] == num[j] == "8")
                or (num[i] == "6" and num[j] == "9")
                or (num[i] == "9" and num[j] == "6")
            ):
                return False
        return True

