class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_pos = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0
