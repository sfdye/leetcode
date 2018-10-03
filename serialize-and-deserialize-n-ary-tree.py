"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """

        def preorder(root):
            if root:
                vals.append("{}.{}".format(root.val, len(root.children)))
                for child in root.children:
                    preorder(child)
            else:
                vals.append("#")

        vals = []
        preorder(root)
        return " ".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """

        def dfs():
            val = vals.next()
            if val == "#":
                return None
            else:
                val, l = map(int, val.split("."))
                node = TreeNode(val)
                node.children = [dfs() for _ in range(l)]
                return node

        vals = iter(data.split())
        return dfs()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
