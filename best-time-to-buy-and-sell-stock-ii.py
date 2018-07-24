class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        buy = - prices[0]
        sell = 0
        for i in range(1, len(prices)):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i])
        return sell
