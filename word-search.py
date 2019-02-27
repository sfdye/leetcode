class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        rows, cols = len(board), len(board[0])

        def dfs(r, c, word):
            if word == "":
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[0]:
                return False
            board[r][c] = "#"
            ret = (
                dfs(r + 1, c, word[1:]) or dfs(r, c + 1, word[1:]) or dfs(r - 1, c, word[1:]) or dfs(r, c - 1, word[1:])
            )
            board[r][c] = word[0]
            return ret

        return any(dfs(r, c, word) for r in range(rows) for c in range(cols))

