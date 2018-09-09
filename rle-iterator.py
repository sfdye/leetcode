class RLEIterator:
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.i = 0
        self.q = 0
        self.A = A

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.i < len(self.A):
            if self.q + n > self.A[self.i]:
                n -= self.A[self.i] - self.q
                self.q = 0
                self.i += 2
            else:
                self.q += n
                return self.A[self.i + 1]
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
