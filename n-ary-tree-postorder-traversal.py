"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []

        def dfs(root):
            if root:
                for node in root.children:
                    dfs(node)
                ans.append(root.val)

        dfs(root)
        return ans
