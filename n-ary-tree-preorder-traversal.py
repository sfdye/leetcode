"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []

        def dfs(root):
            if root:
                ans.append(root.val)
                for node in root.children:
                    dfs(node)

        dfs(root)
        return ans
