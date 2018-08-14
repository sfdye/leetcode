from collections import deque


class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        queue = deque([click])
        directions = [
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
        ]
        N = len(board)
        M = len(board[0])
        while queue:
            x, y = queue.popleft()
            if board[x][y] == "M":
                board[x][y] = "X"
                break

            adjacent_mine = 0
            adjacent = []
            for direction in directions:
                i, j = direction
                if 0 <= x + i < N and 0 <= y + j < M:
                    if board[x + i][y + j] == "M":
                        adjacent_mine += 1
                    elif board[x + i][y + j] == "E":
                        adjacent.append([x + i, y + j])
            if adjacent_mine == 0:
                board[x][y] = "B"
                for x in adjacent:
                    queue.append(x)
                    # avoid adding duplicates
                    board[x[0]][x[1]] = "B"
            else:
                board[x][y] = str(adjacent_mine)

        return board
