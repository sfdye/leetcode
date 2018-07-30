# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        sentinel.next = head

        fast, slow = sentinel, sentinel
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next

        return slow
