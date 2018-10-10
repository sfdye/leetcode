class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = float("inf")
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                elif s < target:
                    l += 1
                else:
                    r -= 1
                if abs(s - target) < abs(res - target):
                    res = s
        return res

