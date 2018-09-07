# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def is_mirror(t1, t2):
            if not t1 and not t2:
                return True
            elif t1 and t2 and t1.val == t2.val:
                return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)
            else:
                return False

        return not root or is_mirror(root.left, root.right)
