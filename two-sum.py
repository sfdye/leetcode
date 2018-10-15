class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for index, num in enumerate(nums):
            if target - num in seen:
                return seen[target - num], index
            else:
                seen[num] = index
