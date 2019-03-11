class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        p = list(range(n))

        def find(u):
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]

        for u, v in edges:
            if find(u) == find(v):
                return False
            p[find(v)] = find(u)
        return len(set(map(find, p))) == 1
