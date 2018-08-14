class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global maxdep
        maxdep = 0

        self.dfs(root, 1)

        return maxdep

    def dfs(self, node, dep):
        global maxdep

        if not node:
            maxdep = max(maxdep, dep - 1)
            return
        else:
            self.dfs(node.left, dep + 1)
            self.dfs(node.right, dep + 1)
