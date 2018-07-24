class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        cur_sum = 0
        seen = {0: -1}
        for i in range(len(nums)):
            cur_sum += nums[i]
            if k != 0:
                cur_sum %= k
            if cur_sum in seen:
                if i - seen[cur_sum] > 1:
                    return True
            else:
                seen[cur_sum] = i
        return False
