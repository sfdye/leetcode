class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        return len(str) == len(pattern) and len(set(pattern)) == len(set(str)) == len(set(zip(pattern, str)))
