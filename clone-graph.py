# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        queue = collections.deque([node])
        node_copy = UndirectedGraphNode(node.label)
        dic = {node: node_copy}
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighbor_copy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighbor_copy
                    dic[node].neighbors.append(neighbor_copy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return node_copy
