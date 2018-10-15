class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        res = max(len(list(g)) for k, g in itertools.groupby(seats) if k == 0)
        return max((res + 1) // 2, seats.index(1), seats[::-1].index(1))
            
            
        