# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = self.second = None
        self.pre = TreeNode(-float("inf"))

        def inorder(root):
            if root:
                inorder(root.left)
                if not self.first and root.val <= self.pre.val:
                    self.first = self.pre
                if self.first and root.val <= self.pre.val:
                    self.second = root
                self.pre = root
                inorder(root.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
