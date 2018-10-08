# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        h = [intervals[0].end]
        for interval in intervals[1:]:
            if h[0] <= interval.start:
                heapq.heapreplace(h, interval.end)
            else:
                heapq.heappush(h, interval.end)
        return len(h)
