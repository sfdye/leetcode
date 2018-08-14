# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        cur = head
        node = head.next

        while node:
            while node and node.val == cur.val:
                node = node.next
            cur.next = node
            cur = node
            if node:
                node = node.next

        return head
