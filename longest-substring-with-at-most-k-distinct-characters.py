class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = {}
        left = right = 0
        maxlen = 0
        while right < len(s):
            d[s[right]] = right
            right += 1
            if len(d) == k + 1:
                min_left = min(d.values())
                left = min_left + 1
                del d[s[min_left]]
            maxlen = max(maxlen, right - left)
        return maxlen
