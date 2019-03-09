# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.ans = float("inf")

        while root:
            if abs(root.val - target) < abs(self.ans - target):
                self.ans = root.val
            if root.val < target:
                root = root.right
            else:
                root = root.left
        return self.ans
