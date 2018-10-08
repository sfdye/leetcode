class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = right = formed = 0
        ans = float("inf"), 0, 0
        cur = collections.defaultdict(int)
        expected = collections.Counter(t)
        required = len(expected)
        while right < len(s):
            ch = s[right]
            cur[ch] += 1
            if ch in expected and cur[ch] == expected[ch]:
                formed += 1
            while left <= right and formed == required:
                if right - left + 1 < ans[0]:
                    ans = right - left + 1, left, right
                ch = s[left]
                cur[ch] -= 1
                if ch in expected and cur[ch] < expected[ch]:
                    formed -= 1
                left += 1
            right += 1
        return s[ans[1] : ans[2] + 1] if ans[0] < float("inf") else ""
