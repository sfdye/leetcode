# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def dfs(self, root, depth):

        if root == None:
            return
        else:
            if len(ans) <= depth:
                ans.append([root.val])
            else:
                ans[depth].append(root.val)

            self.dfs(root.left, depth + 1)
            self.dfs(root.right, depth + 1)

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        global ans

        ans = []

        self.dfs(root, 0)

        for i in range(len(ans)):
            if i % 2 == 1:
                ans[i].reverse()

        return ans
