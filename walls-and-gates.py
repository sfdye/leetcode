class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """

        if not rooms:
            return

        N, M = len(rooms), len(rooms[0])
        INF = 2 ** 31 - 1
        queue = collections.deque()
        for i in range(N):
            for j in range(M):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()
            for dir in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                r = row + dir[0]
                c = col + dir[1]
                if 0 <= r < N and 0 <= c < M and rooms[r][c] == INF:
                    rooms[r][c] = rooms[row][col] + 1
                    queue.append((r, c))
