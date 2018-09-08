# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return (
            abs(self.height(root.left) - self.height(root.right)) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
            if root
            else True
        )

    def height(self, node):
        return 1 + max(self.height(node.left), self.height(node.right)) if node else 0
