class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1
        return [lo, hi] if target in nums[lo : lo + 1] else [-1, -1]
