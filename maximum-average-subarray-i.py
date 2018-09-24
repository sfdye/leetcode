class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum = cur_sum = sum(nums[:k])
        for i in range(len(nums) - k):
            cur_sum = cur_sum - nums[i] + nums[i + k]
            max_sum = max(max_sum, cur_sum)
        return max_sum / k
