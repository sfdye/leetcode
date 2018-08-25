class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        p = list(range(N))

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for i in range(N):
            for j in range(N):
                if M[i][j] == 1:
                    p[find(i)] = p[find(j)]
        return len(set(map(find, p)))
