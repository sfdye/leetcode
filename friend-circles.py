class DSU:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1 for _ in range(N)]
        self.count = N

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.count -= 1


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        dsu = DSU(len(M))
        for i in range(len(M)):
            for j in range(i):
                if M[i][j] == 1:
                    dsu.union(i, j)
        return dsu.count

