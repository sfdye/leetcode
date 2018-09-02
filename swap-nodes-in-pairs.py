# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next, node = head, dummy

        while node and node.next and node.next.next:
            tmp = node.next.next
            node.next.next = tmp.next
            tmp.next = node.next
            node.next = tmp
            node = node.next.next

        return dummy.next
