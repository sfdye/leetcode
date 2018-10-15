# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def get_height(node):
            if not node:
                return 0
            else:
                return get_height(node.left) + 1

        if not root:
            return 0
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        else:
            return (1 << right_height) + self.countNodes(root.left)
