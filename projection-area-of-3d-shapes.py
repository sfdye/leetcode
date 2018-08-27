class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return (
            len(grid) ** 2
            - sum(grid, []).count(0)
            + sum(max(row) for row in grid)
            + sum(max(col) for col in zip(*grid))
        )
