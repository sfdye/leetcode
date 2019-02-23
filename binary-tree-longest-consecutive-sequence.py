# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestConsecutive(self, root: "TreeNode") -> "int":
        self.ans = 0

        def dfs(root):
            if not root:
                return 0
            else:
                left = dfs(root.left) + 1
                right = dfs(root.right) + 1
                if root.left and root.left.val != root.val + 1:
                    left = 1
                if root.right and root.right.val != root.val + 1:
                    right = 1
                cur = max(left, right)
                self.ans = max(self.ans, cur)
                return cur

        dfs(root)

        return self.ans
