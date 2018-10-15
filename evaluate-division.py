class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        d = collections.defaultdict(dict)
        for (a, b), v in zip(equations, values):
            d[a][b] = v
            d[b][a] = 1.0 / v
            d[a][a] = d[b][b] = 1.0
        for k in d:
            for i in d[k]:
                for j in d[k]:
                    d[i][j] = d[i][k] * d[k][j]
        return [d[a].get(b, -1.0) for a, b in queries]
            
            
        
                        