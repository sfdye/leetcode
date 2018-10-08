# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []

        def generate(l, r):
            trees = []
            for root in range(l, r + 1):
                for left in generate(l, root - 1):
                    for right in generate(root + 1, r):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
            return trees or [None]

        return generate(1, n)

