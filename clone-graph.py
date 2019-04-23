"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        dic = {}

        def dfs(node):
            if not node:
                return
            else:
                node_copy = Node(node.val, [])
                dic[node] = node_copy
                for nei in node.neighbors:
                    if nei in dic:
                        node_copy.neighbors.append(dic[nei])
                    else:
                        node_copy.neighbors.append(dfs(nei))
                return node_copy

        return dfs(node)
