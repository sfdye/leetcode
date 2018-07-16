import collections

class Queue(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = collections.deque()    

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        
        self.stack.popleft()

    def peek(self):
        """
        :rtype: int
        """

        return self.stack[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0
