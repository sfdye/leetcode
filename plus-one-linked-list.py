# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def reverse(head):
            pre = None
            while head:
                head.next, head, pre = pre, head.next, head
            return pre

        node = head = reverse(head)
        while node and node.val == 9:
            node.val = 0
            if not node.next:
                node.next = ListNode(0)
            node = node.next
        node.val += 1
        return reverse(head)
