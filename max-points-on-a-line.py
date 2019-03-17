# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution:
    def maxPoints(self, points: List[Point]) -> int:
        d = collections.defaultdict(int)
        ans = 0
        for i in range(len(points)):
            d.clear()
            cur = same = 0
            for j in range(i + 1, len(points)):
                dx, dy = points[i].x - points[j].x, points[i].y - points[j].y
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                gcd = self.get_gcd(dx, dy)
                dx //= gcd
                dy //= gcd
                d[(dx, dy)] += 1
                cur = max(cur, d[(dx, dy)])
            ans = max(ans, cur + same + 1)
        return ans

    def get_gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.get_gcd(b, a % b)
