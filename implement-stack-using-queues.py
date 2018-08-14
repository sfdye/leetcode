class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """

        self.nums.append(x)

    def pop(self):
        """
        :rtype: nothing
        """

        del self.nums[-1]

    def top(self):
        """
        :rtype: int
        """

        return self.nums[-1]

    def empty(self):
        """
        :rtype: bool
        """

        return len(self.nums) == 0
