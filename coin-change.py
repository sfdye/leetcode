class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float("inf")] * amount
        for coin in coins:
            for v in range(coin, amount + 1):
                dp[v] = min(dp[v], dp[v - coin] + 1)
        return dp[-1] if dp[-1] < float("inf") else -1
