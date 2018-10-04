class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == 0:
                    right += 1
                elif left > 0:
                    left -= 1

        self.ans = set()

        def dfs(depth, left, right, left_rem, right_rem, cur):
            if depth == len(s):
                if left_rem == 0 and right_rem == 0:
                    self.ans.add(cur)
            else:
                if s[depth] == "(" and left_rem > 0:
                    dfs(depth + 1, left, right, left_rem - 1, right_rem, cur)
                if s[depth] == ")" and right_rem > 0:
                    dfs(depth + 1, left, right, left_rem, right_rem - 1, cur)
                if s[depth] != "(" and s[depth] != ")":
                    dfs(depth + 1, left, right, left_rem, right_rem, cur + s[depth])
                elif s[depth] == "(":
                    dfs(depth + 1, left + 1, right, left_rem, right_rem, cur + "(")
                elif s[depth] == ")" and right < left:
                    dfs(depth + 1, left, right + 1, left_rem, right_rem, cur + ")")

        dfs(0, 0, 0, left, right, "")
        return list(self.ans)
