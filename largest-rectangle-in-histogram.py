class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                cur = heights[stack.pop()]
                ans = max(ans, cur * (i - stack[-1] - 1))
            stack.append(i)
        heights.pop()
        return ans
