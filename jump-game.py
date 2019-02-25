class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= m:
                m = i
        return m == 0
