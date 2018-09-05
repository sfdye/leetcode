class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False

        n, m = len(board), len(board[0])

        def dfs(i, j, word):
            if word == "":
                return True
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != word[0]:
                return False
            board[i][j] = "#"
            ret = (
                dfs(i - 1, j, word[1:]) or dfs(i, j + 1, word[1:]) or dfs(i + 1, j, word[1:]) or dfs(i, j - 1, word[1:])
            )
            board[i][j] = word[0]
            return ret

        for i in range(n):
            for j in range(m):
                if dfs(i, j, word):
                    return True
        return False
