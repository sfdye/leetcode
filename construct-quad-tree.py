"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """

        def check(a, b, c, d):
            for i in range(a, c):
                for j in range(b, d):
                    if grid[i][j] != grid[a][b]:
                        return False, "*"
            return True, bool(grid[a][b])

        def build(a, b, c, d):
            isLeaf, val = check(a, b, c, d)
            node = Node(val, isLeaf, None, None, None, None)
            if isLeaf:
                return node
            else:
                node.topLeft = build(a, b, (a + c) // 2, (b + d) // 2)
                node.topRight = build(a, (b + d) // 2, (a + c) // 2, d)
                node.bottomLeft = build((a + c) // 2, b, c, (b + d) // 2)
                node.bottomRight = build((a + c) // 2, (b + d) // 2, c, d)
                return node

        return build(0, 0, len(grid), len(grid))
