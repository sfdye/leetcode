class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c = collections.Counter()
        for num in nums:
            c[num] += 1
            if len(c) == 3:
                c -= collections.Counter(set(c))
        return [x for x in c if nums.count(x) > len(nums) / 3]
