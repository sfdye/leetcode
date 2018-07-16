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

        intervals = sorted(intervals, key=lambda x: x.start)

        start = intervals[0].start
        end = intervals[0].end
        result = []

        for i in range(1, len(intervals)):
            # not merging
            if intervals[i].start > end:
                result.append(Interval(start, end))
                start = intervals[i].start
                end = intervals[i].end
            # merge
            else:
                end = max(end, intervals[i].end)

        result.append(Interval(start, end))

        return result
