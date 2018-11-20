class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        
        def dfs(cur, i):
            if i == k:
                ans.append(cur)
            else:
                for j in range(1 + cur[-1] if cur else 1, n+1):
                    dfs(cur + [j], i+1)
        
        dfs([], 0)
        
        return ans
        