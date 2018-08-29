# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = float("inf")
        self.prev = float("inf")

        def inorder(root):
            if root:
                inorder(root.left)
                self.ans = min(self.ans, abs(root.val - self.prev))
                self.prev = root.val
                inorder(root.right)

        inorder(root)
        return self.ans
