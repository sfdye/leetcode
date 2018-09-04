class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0]]
        ans = nums[0]
        for i in range(1, len(nums)):
            dp.append(nums[i] + max(0, dp[-1]))
            ans = max(ans, dp[-1])
        return ans
