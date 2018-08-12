class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 0
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j+1] > nums[j]:
                j += 1
            ans = max(ans, j-i+1)
            i = j + 1
        return ans
