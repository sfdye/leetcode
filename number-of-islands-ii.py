class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}
        self.count = 0

    def add(self, x):
        self.parent[x] = x
        self.size[x] = 1
        self.count += 1

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
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dsu = DSU()
        ans = []
        for x in map(tuple, positions):
            i, j = x
            dsu.add(x)
            for y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if y in dsu.parent:
                    dsu.union(x, y)
            ans.append(dsu.count)
        return ans
