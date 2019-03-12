# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        def _rob(root):
            if not root:
                return 0, 0
            left_yes, left_no = _rob(root.left)
            right_yes, right_no = _rob(root.right)
            return root.val + left_no + right_no, max(left_yes, left_no) + max(right_yes, right_no)

        return max(_rob(root))
