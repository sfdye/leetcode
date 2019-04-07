class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if not s1:
            return True
        d1 = collections.Counter(s1)
        d2 = collections.Counter(s2[: len(s1)])
        for i in range(len(s1), len(s2)):
            if d1 == d2:
                return True
            d2[s2[i]] += 1
            d2[s2[i - len(s1)]] -= 1
            if d2[s2[i - len(s1)]] == 0:
                del d2[s2[i - len(s1)]]
        return d1 == d2
