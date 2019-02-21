class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans, cur_sum, left = float("inf"), 0, 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            while cur_sum >= s:
                ans = min(ans, i - left + 1)
                cur_sum -= nums[left]
                left += 1
        return ans if ans < float("inf") else 0

