class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = start = 0
        d = {}
        for i, ch in enumerate(s):
            if ch in d and start <= d[ch]:
                start = d[ch] + 1
            else:
                ans = max(ans, i - start + 1)
            d[ch] = i
        return ans
