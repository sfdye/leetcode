class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        expected = collections.Counter(t)
        cur = collections.defaultdict(int)
        l = r = 0
        formed = 0
        required = len(expected)
        ans = float("inf"), 0, 0
        while r < len(s):
            c = s[r]
            cur[c] += 1
            if c in expected and cur[c] == expected[c]:
                formed += 1
            while formed == required and l <= r:
                if r - l + 1 < ans[0]:
                    ans = r - l + 1, l, r
                c = s[l]
                cur[c] -= 1
                if c in expected and cur[c] < expected[c]:
                    formed -= 1
                l += 1
            r += 1
        return s[ans[1] : ans[2] + 1] if ans[0] < float("inf") else ""
