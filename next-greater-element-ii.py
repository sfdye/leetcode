class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        nums = nums + nums
        res = [-1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
        return res[: len(nums) // 2]
