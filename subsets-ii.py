class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                last = len(ans)
            for j in range(len(ans) - last, len(ans)):
                ans.append(ans[j] + [nums[i]])
        return ans
