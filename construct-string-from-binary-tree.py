class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """

        def preorder(root):
            if not root:
                return ""
            if not root.left and not root.right:
                return "{}".format(root.val)
            elif not root.right:
                return "{}({})".format(root.val, preorder(root.left))
            else:
                return "{}({})({})".format(root.val, preorder(root.left), preorder(root.right))

        return preorder(t)
