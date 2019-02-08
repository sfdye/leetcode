# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedListToBST(self, head: "ListNode") -> "TreeNode":
        def build_tree(nums):
            if len(nums) == 0:
                return None
            elif len(nums) == 1:
                return TreeNode(nums[0])
            else:
                mid = len(nums) // 2
                root = TreeNode(nums[mid])
                root.left = build_tree(nums[:mid])
                root.right = build_tree(nums[mid + 1 :])
                return root

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return build_tree(nums)
