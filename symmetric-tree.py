# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_mirror(root, root)

    def is_mirror(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        elif t1 == None or t2 == None:
            return False
        else:
            return (
                t1.val == t2.val
                and self.is_mirror(t1.left, t2.right)
                and self.is_mirror(t1.right, t2.left)
            )
