class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        for i, num in enumerate(sorted(nums)[::-1]):
            nums[(i * 2 + 1) % (len(nums) | 1)] = num
