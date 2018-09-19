class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        i = 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j] == nums[j + 1] - 1:
                j += 1
            if i == j:
                ans.append(str(nums[i]))
            else:
                ans.append("{}->{}".format(nums[i], nums[j]))
            i = j + 1
        return ans

