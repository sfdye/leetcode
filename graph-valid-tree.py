class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        p = list(range(n))

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for edge in edges:
            u, v = map(find, edge)
            if u == v:
                return False
            p[u] = p[v]
        return len(set(map(find, p))) == 1
