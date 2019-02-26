class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            x = matrix[mid // n][mid % n]
            if x == target:
                return True
            elif x < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

