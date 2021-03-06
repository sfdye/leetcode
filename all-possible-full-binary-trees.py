# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """

        def build(N):
            if N == 1:
                yield TreeNode(0)
            else:
                for i in range(1, N, 2):
                    for left in build(i):
                        for right in build(N - i - 1):
                            root = TreeNode(0)
                            root.left = left
                            root.right = right
                            yield root

        return list(build(N))
