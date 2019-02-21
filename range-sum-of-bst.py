# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rangeSumBST(self, root: "TreeNode", L: "int", R: "int") -> "int":
        stack, ans, cur = [], 0, root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if L <= cur.val <= R:
                ans += cur.val
            if cur.val > R:
                break
            cur = cur.right
        return ans
