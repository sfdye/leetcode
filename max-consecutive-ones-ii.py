class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, prev, cur = 0, -1, 0
        for num in nums:
            if num == 0:
                prev, cur = cur, 0
            else:
                cur += 1
            ans = max(ans, prev + 1 + cur)
        return ans
