class TicTacToe:
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows, self.cols = [0] * n, [0] * n
        self.diagonal = self.anti_diagonal = 0
        self.size = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        add = 1 if player == 1 else -1
        self.rows[row] += add
        self.cols[col] += add
        if row == col:
            self.diagonal += add
        if row == self.size - 1 - col:
            self.anti_diagonal += add
        if any(x == self.size for x in map(abs, [self.rows[row], self.cols[col], self.diagonal, self.anti_diagonal])):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
