# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        pre.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = cur = ListNode(None)
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        cur.next = left or right
        return dummy.next
