# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def intervalIntersection(self, A: "List[Interval]", B: "List[Interval]") -> "List[Interval]":
        i = j = 0
        ans = []
        while i < len(A) and j < len(B):
            lo = max(A[i].start, B[j].start)
            hi = min(A[i].end, B[j].end)
            if lo <= hi:
                ans.append(Interval(lo, hi))
            if A[i].end < B[j].end:
                i += 1
            else:
                j += 1
        return ans

