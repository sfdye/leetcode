class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)

        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])

        f = [0] * length

        f[0] = nums[0]
        f[1] = max(nums[0], nums[1])
        for i in range(2, length):
            f[i] = max(f[i-1], f[i-2]+nums[i])

        return f[length-1]
