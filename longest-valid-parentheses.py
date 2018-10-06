class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = longest = 0
        for ch in s:
            if ch == "(":
                left += 1
            else:
                right += 1
            if left == right:
                longest = max(longest, left * 2)
            elif right > left:
                left = right = 0
        left = right = 0
        for ch in s[::-1]:
            if ch == "(":
                left += 1
            else:
                right += 1
            if left == right:
                longest = max(longest, left * 2)
            elif left > right:
                left = right = 0
        return longest
