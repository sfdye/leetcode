# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def dfs(root):
            if not root:
                return 0
            left_len = dfs(root.left)
            right_len = dfs(root.right)
            left = left_len + 1 if root.left and root.left.val == root.val else 0
            right = right_len + 1 if root.right and root.right.val == root.val else 0
            self.ans = max(self.ans, left + right)
            return max(left, right)

        dfs(root)
        return self.ans
