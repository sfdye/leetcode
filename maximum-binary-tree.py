# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def build(l, r):
            if l == r:
                return None
            else:
                max_num, max_i = -float("inf"), l
                for i in range(l, r):
                    if nums[i] > max_num:
                        max_num = nums[i]
                        max_i = i
                node = TreeNode(max_num)
                node.left = build(l, max_i)
                node.right = build(max_i + 1, r)
                return node

        return build(0, len(nums))
