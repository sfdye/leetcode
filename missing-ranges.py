class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums.append(upper + 1)
        prev = lower - 1
        ans = []
        for num in nums:
            if num - prev == 2:
                ans.append(str(prev + 1))
            elif num - prev > 2:
                ans.append("{}->{}".format(prev + 1, num - 1))
            prev = num
        return ans

