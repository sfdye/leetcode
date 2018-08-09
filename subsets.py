class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = [[]]
        for i in range(len(nums)):
            ans.append([item + [nums[i]] for item in ans])
        return ans
