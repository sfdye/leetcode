# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(root):
            if not root:
                return 0, 0
            else:
                inc = dec = 1
                if root.left:
                    left_inc, left_dec = dfs(root.left)
                    if root.left.val == root.val + 1:
                        inc = left_inc + 1
                    if root.left.val == root.val - 1:
                        dec = left_dec + 1
                if root.right:
                    right_inc, right_dec = dfs(root.right)
                    if root.right.val == root.val + 1:
                        inc = max(inc, right_inc + 1)
                    if root.right.val == root.val - 1:
                        dec = max(dec, right_dec + 1)
                self.ans = max(self.ans, inc + dec - 1)
                return inc, dec

        dfs(root)
        return self.ans
