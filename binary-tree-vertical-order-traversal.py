# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        d = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            level = []
            for node, col in queue:
                d[col].append(node.val)
                if node.left:
                    level.append((node.left, col - 1))
                if node.right:
                    level.append((node.right, col + 1))
            queue = level
        return [d[col] for col in sorted(d)]
