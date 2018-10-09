class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        p = list(range(n))

        def find(u):
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]

        for i in range(n):
            for j in range(i):
                if M[i][j]:
                    p[find(i)] = p[find(j)]
        return len(set(map(find, p)))
