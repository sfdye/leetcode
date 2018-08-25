class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        p = list(range(1001))

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for edge in edges:
            u, v = map(find, edge)
            if u == v:
                return edge[0], edge[1]
            p[u] = p[v]
