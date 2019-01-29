class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = cur_min = cur_max = nums[0]
        for i in range(1, len(nums)):
            cur_max, cur_min = (
                max(nums[i] * cur_max, nums[i] * cur_min, nums[i]),
                min(nums[i] * cur_max, nums[i] * cur_min, nums[i]),
            )
            res = max(res, cur_max)
        return res
