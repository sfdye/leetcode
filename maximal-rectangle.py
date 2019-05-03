class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        dp = [0 for _ in range(len(matrix[0]))]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0
            ans = max(ans, self.best_rectangle(dp))
        return ans

    def best_rectangle(self, heights):
        max_area = 0
        heights.append(0)
        stack = [-1]
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                cur = heights[stack.pop()]
                max_area = max(max_area, cur * (i - stack[-1] - 1))
            stack.append(i)
        heights.pop()
        return max_area

