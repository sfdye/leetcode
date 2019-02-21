# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumNumbers(self, root: "TreeNode") -> "int":
        self.res = 0

        def dfs(root, cur):
            if not root:
                return
            elif root and not root.left and not root.right:
                self.res += cur * 10 + root.val
                return
            else:
                dfs(root.left, cur * 10 + root.val)
                dfs(root.right, cur * 10 + root.val)

        dfs(root, 0)

        return self.res

