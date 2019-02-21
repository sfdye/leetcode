class Solution:
    def addToArrayForm(self, A: "List[int]", K: "int") -> "List[int]":
        A.reverse()
        for i in range(len(A)):
            K, A[i] = divmod(A[i] + K, 10)
        while K > 0:
            A.append(K % 10)
            K //= 10
        return A[::-1]

