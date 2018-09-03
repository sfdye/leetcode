class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()

        def dfs(cur, target):
            if target < 0:
                return
            if target == 0:
                ans.append(cur)
            for num in candidates:
                if num > target:
                    break
                if not cur or cur[-1] <= num:
                    dfs(cur + [num], target - num)

        dfs([], target)
        return ans
