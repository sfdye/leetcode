class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()

        def dfs(target, arr):
            if target < 0:
                return
            if target == 0:
                ans.append(arr)
            for num in candidates:
                if num > target:
                    break
                if len(arr) == 0 or arr[-1] <= num:
                    dfs(target - num, arr + [num])

        dfs(target, [])
        return ans
