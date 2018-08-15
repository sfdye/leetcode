class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        ans = 0
        for p in points:
            d = collections.defaultdict(int)
            for q in points:
                d[(p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2] += 1
            for k in d.values():
                ans += k * (k - 1)
        return ans
