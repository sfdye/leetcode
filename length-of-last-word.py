class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == "":
            return 0
        else:
            return len(s[s.rfind(" ")+1:])
