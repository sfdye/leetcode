from functools import lru_cache


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        @lru_cache(maxsize=20000)
        def dfs(i, cur):
            if i == len(nums):
                return cur == S
            else:
                return dfs(i + 1, cur + nums[i]) + dfs(i + 1, cur - nums[i])

        return dfs(0, 0)

