# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def dfs(root):
            if root:
                yield from dfs(root.left)
                yield root
                yield from dfs(root.right)

        for node in dfs(root):
            k -= 1
            if k == 0:
                return node.val
