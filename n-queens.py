class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = ["." * n for _ in range(n)]
        cols, diagonal, antidiagonal = set(), set(), set()
        self.ans = []

        def dfs(row):
            if row == n:
                self.ans.append(board[::])
                return
            else:
                for col in range(n):
                    if not col in cols and not row + col in diagonal and not row - col in antidiagonal:
                        cols.add(col)
                        diagonal.add(row + col)
                        antidiagonal.add(row - col)
                        board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                        dfs(row + 1)
                        board[row] = board[row][:col] + "." + board[row][col + 1 :]
                        antidiagonal.remove(row - col)
                        diagonal.remove(row + col)
                        cols.remove(col)

        dfs(0)
        return self.ans
