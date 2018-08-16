class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        str.reverse()
        last = 0
        for i in range(len(str)):
            if str[i] == " ":
                str[last:i] = str[last:i][::-1]
                last = i + 1
        str[last:] = str[last:][::-1]
