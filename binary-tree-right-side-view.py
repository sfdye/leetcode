# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        height = collections.defaultdict(list)

        def dfs(root, depth):
            if root:
                height[depth].append(root.val)
                dfs(root.right, depth + 1)
                dfs(root.left, depth + 1)

        dfs(root, 0)
        return [height[i][0] for i in range(len(height))]
