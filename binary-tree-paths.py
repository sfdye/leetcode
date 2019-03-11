# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        def dfs(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    ans.append(path)
                    return
                else:
                    path += "->"
                    dfs(root.left, path)
                    dfs(root.right, path)

        ans = []
        dfs(root, "")
        return ans
