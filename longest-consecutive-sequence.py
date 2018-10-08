class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        nums = set(nums)
        for num in nums:
            if num - 1 not in nums:
                cur = num
                cur_streak = 1
                while cur + 1 in nums:
                    cur_streak += 1
                    cur += 1
                longest_streak = max(longest_streak, cur_streak)
        return longest_streak
