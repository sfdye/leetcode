class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """

        def dist(x, y):
            return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5

        def area(a, b, c):
            p = (a + b + c) / 2.0
            # this sucks
            if p < a or p < b or p < c:
                return 0
            return (p * (p - a) * (p - b) * (p - c)) ** 0.5

        max_area = 0
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a = dist(points[i], points[j])
                    b = dist(points[i], points[k])
                    c = dist(points[j], points[k])
                    max_area = max(max_area, area(a, b, c))
        return max_area
