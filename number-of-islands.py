class Solution(object):
    def dfs(self, grid, x, y):

        if visited[x][y] == 1:
            return

        # print 'visit ', x, y
        visited[x][y] = 1

        if 0 <= x-1 < n and 0 <= y < m and grid[x-1][y] == '1':
            self.dfs(grid, x-1, y)

        if 0 <= x+1 < n and 0 <= y < m and grid[x+1][y] == '1':
            self.dfs(grid, x+1, y)

        if 0 <= x < n and 0 <= y-1 < m and grid[x][y-1] == '1':
            self.dfs(grid, x, y-1)

        if 0 <= x < n and 0 <= y+1 < m and grid[x][y+1] == '1':
            self.dfs(grid, x, y+1)


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        global n,m

        n = len(grid)

        if n == 0:
            return 0

        m = len(grid[0])

        global visited

        visited = [[0] * m for i in range(n)]


        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    ans += 1
                    print 'dfs', i,j
                    self.dfs(grid, i, j)

        return ans
