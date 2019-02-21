class Solution:
    def minCost(self, costs: 'List[List[int]]') -> 'int':
        min_r = min_g = min_b = 0
        for r, g, b in costs:
            min_r, min_g, min_b = min(min_g,min_b)+r, min(min_r,  min_b) + g, min(min_r, min_g) + b
        return min(min_r, min_g, min_b)
        