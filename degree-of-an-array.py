class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.defaultdict(int)
        first = {}
        degree = -float("inf")
        ans = float("inf")
        for i, num in enumerate(nums):
            c[num] += 1
            first.setdefault(num, i)
            if c[num] > degree or (c[num] == degree and i - first[num] + 1 < ans):
                degree = c[num]
                ans = i - first[num] + 1
        return ans
