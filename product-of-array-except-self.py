class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = p * res[i]
            p = p * nums[i]
        return res
