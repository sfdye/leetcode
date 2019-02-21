class Solution:
    def hIndex(self, citations: "List[int]") -> "int":
        citations.sort(reverse=True)
        h = len(citations) - 1
        while h >= 0:
            if citations[h] > h:
                break
            h -= 1
        return h + 1
