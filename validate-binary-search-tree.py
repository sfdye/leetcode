# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def validate(node, min_value, max_value):
            if not node:
                return True
            if not (min_value < node.val < max_value):
                return False
            return validate(node.left, min_value, node.val) and validate(
                node.right, node.val, max_value
            )

        return validate(root, -float("inf"), float("inf"))
