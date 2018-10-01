class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        w = collections.defaultdict(dict)
        for u, v, p in flights:
            w[u][v] = p
        heap = [(0, src, K + 1)]
        seen = set()
        while heap:
            p, u, K = heapq.heappop(heap)
            seen.add(u)
            if u == dst:
                return p
            if K > 0:
                for v in w[u]:
                    if v not in seen:
                        heapq.heappush(heap, (p + w[u][v], v, K - 1))
        return -1

