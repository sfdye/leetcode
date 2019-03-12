class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        prev_max, cur_max = 0, 0
        for num in nums:
            cur_max, prev_max = max(prev_max + num, cur_max), cur_max
        return cur_max

