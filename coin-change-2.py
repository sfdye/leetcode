class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [1] + [0] * amount
        for coin in coins:
            for v in range(coin, amount + 1):
                dp[v] += dp[v - coin]
        return dp[-1]

