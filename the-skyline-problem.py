class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        ans = [[0, 0]]
        live = [(0, float("inf"))]
        for pos, negH, R in events:
            while live[0][1] <= pos:
                heapq.heappop(live)
            if negH:
                heapq.heappush(live, (negH, R))
            if ans[-1][1] != -live[0][0]:
                ans.append([pos, -live[0][0]])
        return ans[1:]
