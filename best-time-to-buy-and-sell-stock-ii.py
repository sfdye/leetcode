class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy, sell = -prices[0], 0
        for price in prices[1:]:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price)
        return sell

