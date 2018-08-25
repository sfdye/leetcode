class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        n, m = len(nums), len(nums[0]) if nums else 0

        if r * c != n * m:
            return nums
        flatten = sum(nums, [])
        return [flatten[c * i : c * (i + 1)] for i in range(r)]
