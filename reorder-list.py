# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        middle = self._break(head)
        l1, l2 = head, self._reverse(middle)
        self._merge(l1, l2)

    def _break(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        return middle

    def _reverse(self, head):
        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        return pre

    def _merge(self, l1, l2):
        while l2:
            n1 = l1.next
            n2 = l2.next
            l1.next = l2
            l2.next = n1
            l1, l2 = n1, n2

