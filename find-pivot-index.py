class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cur_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            if cur_sum == total_sum - nums[i] - cur_sum:
                return i
            cur_sum += nums[i]
        return -1
