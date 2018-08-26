# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def check(p, q):
            if not p and not q:
                return True
            if (p == None) ^ (q == None):
                return False
            return p.val == q.val and check(p.left, q.left) and check(p.right, q.right)

        return check(p, q)
