class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        nums = [a * x * x + b * x + c for x in nums]
        ans = [0 for _ in range(len(nums))]
        i, j = 0, len(nums) - 1
        k, d = (-1, -1) if a > 0 else (0, 1)
        while i <= j:
            if nums[i] * -d > nums[j] * -d:
                ans[k] = nums[i]
                i += 1
            else:
                ans[k] = nums[j]
                j -= 1
            k += d
        return ans

