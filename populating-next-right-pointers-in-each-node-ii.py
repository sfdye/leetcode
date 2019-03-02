"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        node = root
        while node:
            dummy = pre = TreeLinkNode(0)
            while node:
                if node.left:
                    pre.next = node.left
                    pre = pre.next
                if node.right:
                    pre.next = node.right
                    pre = pre.next
                node = node.next
            node = dummy.next
        return root
