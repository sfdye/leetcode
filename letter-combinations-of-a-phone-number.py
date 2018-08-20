class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        self.ans = []

        def dfs(s, cur):
            if len(s) == 0:
                self.ans.append(cur)
                return
            else:
                for c in m[s[0]]:
                    dfs(s[1:], cur + c)

        if not digits:
            return []

        dfs(digits, "")
        return self.ans
