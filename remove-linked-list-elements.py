# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = prev = ListNode(0)
        dummy.next = head
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return dummy.next
