# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            hl = self.get_depth(root.left)
            hr = self.get_depth(root.right)
            if hl == hr:
                return (1 << hl) + self.countNodes(root.right)
            else:
                return (1 << hr) + self.countNodes(root.left)

    def get_depth(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height

