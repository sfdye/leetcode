class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0: -1}
        ans = acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            if acc - k in d:
                ans = max(ans, i - d[acc - k])
            if acc not in d:
                d[acc] = i
        return ans
