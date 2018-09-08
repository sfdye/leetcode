# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level, ans = [root], []
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return ans[::-1]
