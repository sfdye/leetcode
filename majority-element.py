class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        ans = None
        for num in nums:
            if count == 0:
                ans = num
            count += 1 if num == ans else -1
        return ans
