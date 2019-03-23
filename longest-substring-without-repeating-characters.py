class Solution:
    def lengthOfLongestSubstring(self, s: "str") -> "int":
        left = right = max_len = 0
        d = collections.defaultdict(int)
        for right in range(len(s)):
            left = max(left, d[s[right]])
            max_len = max(max_len, right - left + 1)
            d[s[right]] = right + 1
        return max_len

