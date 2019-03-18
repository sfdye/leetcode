class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        nums = [a * x * x + b * x + c for x in nums]
        left, right = 0, len(nums) - 1
        ans = []
        while left <= right:
            if (a > 0) ^ (nums[left] < nums[right]):
                ans.append(nums[left])
                left += 1
            else:
                ans.append(nums[right])
                right -= 1
        return ans if a <= 0 else ans[::-1]

