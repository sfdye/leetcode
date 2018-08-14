class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return ans
