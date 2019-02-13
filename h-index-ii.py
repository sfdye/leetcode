class Solution:
    def hIndex(self, citations: "List[int]") -> "int":
        n = len(citations)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if citations[mid] >= n - mid:
                hi = mid - 1
            else:
                lo = mid + 1
        return n - lo

