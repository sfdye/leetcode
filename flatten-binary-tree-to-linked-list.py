# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        else:
            left = root.left
            right = root.right
            self.flatten(left)
            self.flatten(right)
            root.left = None
            root.right = left
            cur = root
            while cur.right:
                cur = cur.right
            cur.right = right
