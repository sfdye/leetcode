class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        d = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            d[x][y] = v
            d[y][x] = 1.0 / v
            d[x][x] = d[y][y] = 1.0
        for k in d:
            for i in d[k]:
                for j in d[k]:
                    d[i][j] = d[i][k] * d[k][j]
        return [d[x].get(y, -1.0) for x, y in queries]
