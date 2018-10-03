# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        else:
            node = TreeNode(preorder[0])
            p = inorder.index(preorder[0])
            node.left = self.buildTree(preorder[1 : p + 1], inorder[:p])
            node.right = self.buildTree(preorder[p + 1 :], inorder[p + 1 :])
            return node
