class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        def dfs(s, memo):
            if s in memo:
                return memo[s]
            if not s:
                return []
            ret = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                elif len(word) == len(s):
                    ret.append(word)
                else:
                    sublist = dfs(s[len(word) :], memo)
                    for item in sublist:
                        ret.append(word + " " + item)
            memo[s] = ret
            return ret

        return dfs(s, memo={})
