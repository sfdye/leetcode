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

        def build(nums):
            if nums:
                max_i = nums.index(max(nums))
                node = TreeNode(nums[max_i])
                node.left = build(nums[:max_i])
                node.right = build(nums[max_i+1:])
                return node

        return build(nums)
