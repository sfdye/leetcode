class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums) - 1):
            if (i % 2 == 0 and nums[i] > nums[i + 1]) or (
                i % 2 == 1 and nums[i] < nums[i + 1]
            ):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
