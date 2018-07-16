from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
            
        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                for x in d[diff]:
                    if x != i:
                        return [x, i]
