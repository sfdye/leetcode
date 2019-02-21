# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, inorder: "List[int]", postorder: "List[int]") -> "TreeNode":
        if inorder:
            root = TreeNode(postorder[-1])
            p = inorder.index(root.val)
            root.left = self.buildTree(inorder[:p], postorder[:p])
            root.right = self.buildTree(inorder[p + 1 :], postorder[p:-1])
            return root
