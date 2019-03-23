class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = {}
        left = right = maxlen = 0
        while right < len(s):
            d[s[right]] = right
            right += 1
            if len(d) == 3:
                min_left = min(d.values())
                left = min_left + 1
                del d[s[min_left]]
            maxlen = max(maxlen, right - left)
        return maxlen
