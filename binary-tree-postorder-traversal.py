# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ans = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            cur = stack.pop()
            if cur:
                ans.append(cur.val)
                stack.append(cur)
                stack.append(right)

        return ans[::-1]
