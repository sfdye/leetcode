class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            a, b = b, min(a, b) + cost[i]
        return min(a, b)

