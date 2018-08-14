class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0

        max_value = max(height)
        max_index = height.index(max_value)
        total = max_value * len(height)
        left = 0
        right = len(height) - 1
        mid = max_index
        cur = left + 1
        untraped = 0
        while cur <= mid:
            while cur < mid and height[cur] <= height[left]:
                cur += 1
            untraped += (height[cur] - height[left]) * cur
            left = cur
            cur += 1

        cur = right - 1
        while mid <= cur:
            while mid < cur and height[cur] <= height[right]:
                cur -= 1
            untraped += (height[cur] - height[right]) * (len(height) - cur - 1)
            right = cur
            cur -= 1
        return total - untraped - sum(height)
