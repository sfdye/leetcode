class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        n, m = len(matrix), len(matrix[0])
        lo, hi = 0, n * m - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            num = matrix[mid // m][mid % m]
            if num == target:
                return True
            elif num > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
