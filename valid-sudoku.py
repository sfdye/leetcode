class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def is_valid(s):
            s = s.replace(".", "")
            return sorted(s) == sorted(set(s))

        for row in board:
            if not is_valid("".join(row)):
                return False

        for col in zip(*board):
            if not is_valid("".join(col)):
                return False

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                if not is_valid("".join([board[i][j] for i in range(r, r + 3) for j in range(c, c + 3)])):
                    return False
        return True
