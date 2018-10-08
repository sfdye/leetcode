class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        p = list(range(1001))

        def find(u):
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]

        for edge in edges:
            u, v = map(find, edge)
            if u == v:
                return edge
            p[u] = p[v]
