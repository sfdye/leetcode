class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            for s in strs:
                if s[i] != c:
                    return shortest[:i]
        return shortest
