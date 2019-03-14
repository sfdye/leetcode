class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(num, 0, j) for j, num in enumerate(matrix[0])]
        heapq.heapify(heap)
        for _ in range(k):
            cur, i, j = heapq.heappop(heap)
            if i + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
        return cur

