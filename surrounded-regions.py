class Solution:
    def solve(self, board: "List[List[str]]") -> "None":
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        queue = collections.deque()
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and board[r][c] == "O":
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            board[r][c] = "S"
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if 0 <= r + dr < m and 0 <= c + dc < n and board[r + dr][c + dc] == "O":
                    queue.append((r + dr, c + dc))
        for r in range(m):
            for c in range(n):
                if board[r][c] != "S":
                    board[r][c] = "X"
                else:
                    board[r][c] = "O"

