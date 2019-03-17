# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        s, e = newInterval.start, newInterval.end
        left, right = [], []
        for interval in intervals:
            if interval.end < s:
                left.append(interval)
            elif interval.start > e:
                right.append(interval)
            else:
                s = min(s, interval.start)
                e = max(e, interval.end)
        return left + [Interval(s, e)] + right
