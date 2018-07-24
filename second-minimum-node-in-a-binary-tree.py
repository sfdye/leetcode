# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        min1 = root.val
        self.ans = float('inf')

        def dfs(node):
            if not node:
                return
            if min1 < node.val < self.ans:
                self.ans = node.val
            elif node.val == min1:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1
