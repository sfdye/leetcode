class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = [0] * len(nums)
        max_sum = dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(dp[i - 1], 0)
            max_sum = max(max_sum, dp[i])
        return max_sum
