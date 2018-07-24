# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def traverse(node, leaves):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            traverse(node.left, leaves)
            traverse(node.right, leaves)

        tree1_result = []
        tree2_result = []
        traverse(root1, tree1_result)
        traverse(root2, tree2_result)
        return tree1_result == tree2_result
