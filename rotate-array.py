class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p = k % len(nums)
        tmp = nums[-p:]
        del nums[-p:]
        for x in reversed(tmp):
            nums.insert(0, x)
