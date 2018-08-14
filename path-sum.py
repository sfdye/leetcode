class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        else:
            return self.dfs(root, 0, sum)

    def dfs(self, node, now, sum):
        if node == None:
            return False
        if node.left == None and node.right == None:
            if now + node.val == sum:
                return True
            else:
                return False
        else:
            return self.dfs(node.left, now + node.val, sum) or self.dfs(
                node.right, now + node.val, sum
            )
