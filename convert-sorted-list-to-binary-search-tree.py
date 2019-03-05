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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def build(l, r):
            nonlocal head

            if l <= r:
                m = (l + r) // 2
                left = build(l, m - 1)
                root = TreeNode(head.val)
                root.left = left
                head = head.next
                root.right = build(m + 1, r)
                return root

        n = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            n += 1

        return build(0, n - 1)
