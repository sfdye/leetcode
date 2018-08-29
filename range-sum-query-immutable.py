class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.acc = [0]
        for num in nums:
            self.acc.append(self.acc[-1] + num)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.acc[j + 1] - self.acc[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
