class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        p = list(range(n))

        def find(u):
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]

        for u, v in edges:
            p[find(u)] = p[find(v)]
        return len(set(map(find, p)))
