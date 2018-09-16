class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        left = [None] * N
        stack = []
        for i in range(N):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        right = [None] * N
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and A[i] < A[stack[-1]]:
                stack.pop()
            right[i] = stack[-1] if stack else N
            stack.append(i)

        return sum(A[i] * (i - left[i]) * (right[i] - i) for i in range(N)) % (10 ** 9 + 7)
