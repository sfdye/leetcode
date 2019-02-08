class Solution:
    def sortColors(self, nums: "List[int]") -> "None":
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        n = len(nums) - 1
        while j <= n:
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > 1:
                nums[j], nums[n] = nums[n], nums[j]
                n -= 1
            else:
                j += 1

