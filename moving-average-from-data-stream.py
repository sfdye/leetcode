class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.vec = [0] * size
        self.size = size
        self.len = 0
        self.sum = 0

    def next(self, val: int) -> float:
        self.sum -= self.vec[self.len % self.size]
        self.vec[self.len % self.size] = val
        self.sum += val
        self.len += 1
        return self.sum / min(self.size, self.len)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
