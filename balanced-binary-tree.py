
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        balanced, _ = self.validate(root)

        return balanced

    def validate(self, root):
        if not root:
            return True, 0

        balanced, leftHeight = self.validate(root.left)
        if not balanced:
            return False, 0

        balanced, rightHeight = self.validate(root.right)
        if not balanced:
            return False, 0

        return abs(leftHeight-rightHeight)<=1, max(leftHeight, rightHeight)+1
