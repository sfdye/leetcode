# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        node = head
        l = 1
        while node.next:
            node = node.next
            l += 1
        node.next = head
        for _ in range(l - k % l):
            node = node.next
        head = node.next
        node.next = None
        return head
