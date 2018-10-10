"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        def inorder(node):
            head, tail = node, node
            if node.left:
                hl, tl = inorder(node.left)
                tl.right = node
                node.left = tl
                head = hl
            if node.right:
                hr, tr = inorder(node.right)
                node.right = hr
                hr.left = node
                tail = tr
            head.left = tail
            tail.right = head
            return head, tail

        if not root:
            return None
        else:
            return inorder(root)[0]

