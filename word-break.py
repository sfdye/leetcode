class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        ok = [True]
        words = set(wordDict)
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]
