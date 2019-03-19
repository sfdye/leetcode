class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2 + 1):
            j = len(s) - 1 - i
            if s[i] != s[j]:
                return s[i + 1 : j + 1] == s[i + 1 : j + 1][::-1] or s[i:j] == s[i:j][::-1]
        return True
