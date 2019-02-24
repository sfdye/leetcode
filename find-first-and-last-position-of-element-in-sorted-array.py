class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target <= nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        left = lo
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target >= nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        right = lo - 1
        return [left, right]

