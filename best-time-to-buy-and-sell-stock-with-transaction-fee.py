class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        buy = [0] * len(prices)
        sell = [0] * len(prices)

        buy[0] = -prices[0]
        for i in range(1, len(prices)):
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i] - fee)
        return sell[-1]
