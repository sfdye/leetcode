"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        node = head
        dic = {}
        while node:
            dic[node] = Node(node.val, None, None)
            node = node.next
        node = head
        while node:
            dic[node].next = dic.get(node.next)
            dic[node].random = dic.get(node.random)
            node = node.next
        return dic.get(head)

