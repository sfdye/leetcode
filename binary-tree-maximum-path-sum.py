# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -float("inf")

        def dfs(root):
            if not root:
                return 0
            else:
                left = max(dfs(root.left), 0)
                right = max(dfs(root.right), 0)
                self.ans = max(self.ans, root.val + left + right)
                return root.val + max(left, right)

        dfs(root)
        return self.ans
