class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        d = collections.defaultdict(int)
        d[0] = 1
        s = 0
        ans = 0
        for num in A:
            s += num
            s %= K
            if s in d:
                ans += d[s]
            d[s] += 1
        return ans
