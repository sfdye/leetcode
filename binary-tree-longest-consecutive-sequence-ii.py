# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            else:
                inc = dec = 1
                for child in root.left, root.right:
                    if child:
                        child_inc, child_dec = dfs(child)
                        if child.val == root.val + 1:
                            inc = max(inc, child_inc + 1)
                        if child.val == root.val - 1:
                            dec = max(dec, child_dec + 1)
                self.ans = max(self.ans, inc + dec - 1)
                return inc, dec

        self.ans = 0
        dfs(root)
        return self.ans
