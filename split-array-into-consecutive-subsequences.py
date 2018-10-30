class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = collections.Counter(nums)
        end = collections.Counter()
        for x in nums:
            if count[x] == 0:
                continue
            count[x] -= 1
            if end[x - 1] > 0:
                end[x - 1] -= 1
                end[x] += 1
            elif count[x + 1] > 0 and count[x + 2] > 0:
                count[x + 1] -= 1
                count[x + 2] -= 1
                end[x + 2] += 1
            else:
                return False
        return True

