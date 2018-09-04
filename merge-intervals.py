# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        ans = []
        start, end = intervals[0].start, intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start <= end:
                end = max(end, intervals[i].end)
            else:
                ans.append([start, end])
                start, end = intervals[i].start, intervals[i].end
        ans.append([start, end])
        return ans
