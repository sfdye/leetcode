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
        if not root:
            return True
        else:
            return (
                abs(self.depth(root.left) - self.depth(root.right)) <= 1
                and self.isBalanced(root.left)
                and self.isBalanced(root.right)
            )

    def depth(self, node):
        return 1 + max(self.depth(node.left), self.depth(node.right)) if node else 0
