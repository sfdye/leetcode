class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        count = collections.defaultdict(int)
        for row in wall:
            acc = 0
            for i in range(len(row) - 1):
                acc += row[i]
                count[acc] += 1
        return len(wall) - max(count.values(), default=0)
