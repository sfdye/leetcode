class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = 0
        for center in range(len(s)*2-1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                ans += 1
        return ans
