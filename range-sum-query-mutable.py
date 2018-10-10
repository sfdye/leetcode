class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.n = len(self.nums)
        self.sum_array = [0] * (self.n+1)
        for i in range(self.n):
            self._add(i+1, self.nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self._add(i+1, val-self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums:
            return 0
        else:
            return self._sum(j+1) - self._sum(i)
        
    def _add(self, x, val):
        while x <= self.n:
            self.sum_array[x] += val
            x += self._low_bit(x)
        
    def _sum(self, x):
        res = 0
        while x:
            res += self.sum_array[x]
            x -= self._low_bit(x)
        return res

    def _low_bit(self, x):
        return x & -x


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
