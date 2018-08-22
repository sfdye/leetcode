"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = collections.deque([root])
        ans = []
        while queue:
            nodes = []
            while queue:
                nodes.append(queue.popleft())
            ans.append([node.val for node in nodes])
            for node in nodes:
                for child in node.children:
                    queue.append(child)
        return ans
