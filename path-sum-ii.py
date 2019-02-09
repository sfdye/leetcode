# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: "TreeNode", sum: "int") -> "List[List[int]]":
        res = []

        if not root:
            return []

        def dfs(root, sum, cur):
            if sum == root.val and not root.left and not root.right:
                res.append(cur + [root.val])
                return
            else:
                if root.left:
                    dfs(root.left, sum - root.val, cur + [root.val])
                if root.right:
                    dfs(root.right, sum - root.val, cur + [root.val])

        dfs(root, sum, [])

        return res

