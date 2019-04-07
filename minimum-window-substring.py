class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = right = formed = 0
        ans = float("inf"), 0, 0
        cur = collections.defaultdict(int)
        expected = collections.Counter(t)
        while right < len(s):
            c = s[right]
            cur[c] += 1
            if cur[c] == expected[c]:
                formed += 1
            while left <= right and formed == len(expected):
                if right - left + 1 < ans[0]:
                    ans = right - left + 1, left, right
                c = s[left]
                cur[c] -= 1
                if cur[c] < expected[c]:
                    formed -= 1
                left += 1
            right += 1
        return s[ans[1] : ans[2] + 1] if ans[0] < float("inf") else ""

