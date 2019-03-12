class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self._rob(nums[1:]), self._rob(nums[:-1]))

    def _rob(self, nums):
        prev_max, cur_max = 0, 0
        for num in nums:
            cur_max, prev_max = max(prev_max + num, cur_max), cur_max
        return cur_max
