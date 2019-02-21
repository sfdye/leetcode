class Solution:
    def sumEvenAfterQueries(self, A: "List[int]", queries: "List[List[int]]") -> "List[int]":
        even_sum = sum(x for x in A if x % 2 == 0)
        res = []
        for val, idx in queries:
            if A[idx] % 2 == 0:
                even_sum -= A[idx]
            A[idx] += val
            if A[idx] % 2 == 0:
                even_sum += A[idx]
            res.append(even_sum)
        return res
