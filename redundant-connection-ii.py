class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        def find(u):
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]

        def detect_cycle(edge):
            u, v = edge
            while u != v and u in parents:
                u = parents[u]
            return u == v

        candidates = []
        parents = {}
        for u, v in edges:
            if v not in parents:
                parents[v] = u
            else:
                candidates.append((parents[v], v))
                candidates.append((u, v))

        if candidates:
            return candidates[0] if detect_cycle(candidates[0]) else candidates[1]
        else:
            p = list(range(len(edges)))
            for edge in edges:
                u, v = map(find, edge)
                if u == v:
                    return edge
                p[u] = p[v]
