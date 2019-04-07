class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = [0 for _ in range(32)]
        N = len(nums)
        for num in nums:
            i = 0
            while num:
                ones[i] += num & 1
                i += 1
                num >>= 1
        return sum(ones[i] * (N - ones[i]) for i in range(32))
