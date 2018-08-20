# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        p = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1 : p + 1], post[:p])
        root.right = self.constructFromPrePost(pre[p + 1 :], post[p:-1])
        return root
