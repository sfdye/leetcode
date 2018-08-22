class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.data = [(len(v), iter(v)) for v in [v1, v2] if v]

    def next(self):
        """
        :rtype: int
        """

        len, iter = self.data.pop(0)
        if len > 1:
            self.data.append((len - 1, iter))
        return next(iter)

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.data)


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
