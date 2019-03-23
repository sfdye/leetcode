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
        vals = []

        def preorder(root):
            if root:
                vals.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
            else:
                vals.append("#")

        preorder(root)
        return " ".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split(" "))

        def dfs():
            val = next(vals)
            if val == "#":
                return None
            else:
                root = TreeNode(val)
                root.left = dfs()
                root.right = dfs()
                return root

        return dfs()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
