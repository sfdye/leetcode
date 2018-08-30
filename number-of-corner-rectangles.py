class Solution:
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        counter = collections.Counter()
        for row in grid:
            for c1, v1 in enumerate(row):
                if v1:
                    for c2 in range(c1 + 1, len(row)):
                        if row[c2]:
                            ans += counter[c1, c2]
                            counter[c1, c2] += 1
        return ans
