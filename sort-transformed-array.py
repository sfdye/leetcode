class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        nums = [a*x**2+b*x+c for x in nums]
        ans = [0] * len(nums)
        left, right = 0, len(nums) - 1 
        i, d = (-1, -1) if a > 0 else (0, 1)
        while left <= right:
            if nums[left] * -d > nums[right] * -d:
                ans[i] = nums[left]
                left += 1
            else:
                ans[i] = nums[right]
                right -= 1
            i += d
        return ans
                
                
                