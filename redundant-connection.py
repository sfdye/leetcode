class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return False
            if size[x] < size[y]:
                x, y = y, x
            parent[y] = x
            size[x] += size[y]
            return True

        N = len(edges)
        parent = list(range(N + 1))
        size = [1 for _ in range(N + 1)]
        for x, y in edges:
            if not union(x, y):
                return [x, y]

