class MaxStack(list):
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.append((x, max(x, self[-1][1] if self else x)))

    def pop(self):
        """
        :rtype: int
        """
        return list.pop(self)[0]

    def top(self):
        """
        :rtype: int
        """
        return self[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        return self[-1][1]

    def popMax(self):
        """
        :rtype: int
        """
        m = self[-1][1]
        tmp = []
        while self[-1][0] != m:
            tmp.append(self.pop())
        self.pop()
        map(self.push, tmp[::-1])
        return m


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
