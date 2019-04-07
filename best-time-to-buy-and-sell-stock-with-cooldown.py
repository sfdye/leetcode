class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        b0 = b1 = -prices[0]
        s0 = s1 = s2 = 0
        for i in range(1, len(prices)):
            b0 = max(b1, s2 - prices[i])
            s0 = max(s1, b1 + prices[i])
            s2, s1 = s1, s0
            b1 = b0
        return s0
