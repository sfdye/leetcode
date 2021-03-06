# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def preorder(root):
            if root:
                vals.append(str(root.val))
                preorder(root.left)
                preorder(root.right)

        vals = []
        preorder(root)
        return " ".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = map(int, data.split())
        inorder = sorted(preorder)

        def dfs(preorder, inorder):
            if not inorder:
                return None
            else:
                node = TreeNode(preorder[0])
                p = inorder.index(preorder[0])
                node.left = dfs(preorder[1 : p + 1], inorder[:p])
                node.right = dfs(preorder[p + 1 :], inorder[p + 1 :])
                return node

        return dfs(preorder, inorder)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
