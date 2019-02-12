class Vector2D:
    def __init__(self, v: "List[List[int]]"):
        self.v = v
        self.row = 0
        self.col = 0

    def next(self) -> "int":
        if self.hasNext():
            tmp = self.v[self.row][self.col]
            self.col += 1
            return tmp

    def hasNext(self) -> "bool":
        while self.row < len(self.v):
            if self.col < len(self.v[self.row]):
                return True
            self.row += 1
            self.col = 0
        return False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
