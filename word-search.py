class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if not board:
            return False

        N, M = len(board), len(board[0])

        def dfs(i, j, word, board, cur):
            if cur == len(word):
                return True
            if i < 0 or i >= N or j < 0 or j >= M or board[i][j] != word[cur]:
                return False
            board[i][j] = "#"
            ret = dfs(i+1, j, word, board, cur+1) or dfs(i, j+1, word, board, cur +
                                                         1) or dfs(i-1, j, word, board, cur+1) or dfs(i, j-1, word, board, cur+1)
            board[i][j] = word[cur]
            return ret

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, word, board, 0):
                    return True
        return False
