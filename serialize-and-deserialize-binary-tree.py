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
            else:
                vals.append("#")

        vals = []
        preorder(root)
        return " ".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def dfs():
            val = vals.next()
            if val == "#":
                return None
            else:
                node = TreeNode(val)
                node.left = dfs()
                node.right = dfs()
                return node

        vals = iter(data.split())
        return dfs()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
