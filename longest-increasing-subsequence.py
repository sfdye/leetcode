import bisect


class Solution:
    def lengthOfLIS(self, nums: "List[int]") -> "int":
        if not nums:
            return 0
        dp = []
        for num in nums:
            p = bisect.bisect_left(dp, num)
            if p == len(dp):
                dp.append(num)
            else:
                dp[p] = num
        return len(dp)
