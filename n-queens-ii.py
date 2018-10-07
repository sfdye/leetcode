class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols, diagonal, antidiagonal = set(), set(), set()
        self.ans = 0

        def dfs(row):
            if row == n:
                self.ans += 1
                return
            else:
                for col in range(n):
                    if not col in cols and not row + col in diagonal and not row - col in antidiagonal:
                        cols.add(col)
                        diagonal.add(row + col)
                        antidiagonal.add(row - col)
                        dfs(row + 1)
                        antidiagonal.remove(row - col)
                        diagonal.remove(row + col)
                        cols.remove(col)

        dfs(0)
        return self.ans
