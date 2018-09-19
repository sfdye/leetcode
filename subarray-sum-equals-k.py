class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = collections.defaultdict(int)
        d[0] = 1
        count = cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in d:
                count += d[cur_sum - k]
            d[cur_sum] += 1
        return count

