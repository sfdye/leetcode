# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        d = collections.defaultdict(list)

        def dfs(node, depth):
            if node:
                d[depth].append(node.val)
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root, 0)
        return list(map(lambda x: sum(x) / len(x), d.values()))
