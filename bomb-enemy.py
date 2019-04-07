class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            c = 0
            for j in range(cols):
                if grid[i][j] == "W":
                    c = 0
                elif grid[i][j] == "E":
                    c += 1
                count[i][j] += c
        for i in range(rows):
            c = 0
            for j in range(cols - 1, -1, -1):
                if grid[i][j] == "W":
                    c = 0
                elif grid[i][j] == "E":
                    c += 1
                count[i][j] += c
        for j in range(cols):
            c = 0
            for i in range(rows):
                if grid[i][j] == "W":
                    c = 0
                elif grid[i][j] == "E":
                    c += 1
                count[i][j] += c
        ans = 0
        for j in range(cols):
            c = 0
            for i in range(rows - 1, -1, -1):
                if grid[i][j] == "W":
                    c = 0
                elif grid[i][j] == "E":
                    c += 1
                count[i][j] += c
                if grid[i][j] == "0":
                    ans = max(ans, count[i][j])
        return ans
