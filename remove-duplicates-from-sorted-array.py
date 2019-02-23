class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if slow == 0 or nums[fast] != nums[slow - 1]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
