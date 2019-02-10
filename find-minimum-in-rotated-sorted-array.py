class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        if len(nums) == 1 or nums[lo] < nums[hi]:
            return nums[0]
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[lo]:
                hi = mid - 1
            else:
                lo = mid + 1

