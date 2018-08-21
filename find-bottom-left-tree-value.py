# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.max_depth = 0
        self.ans = root.val

        def dfs(root, depth):
            if not root:
                return
            if depth > self.max_depth:
                self.max_depth = depth
                self.ans = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        return self.ans
