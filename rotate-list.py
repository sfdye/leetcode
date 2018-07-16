class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        p = head
        length = 0
        while p:
            length += 1
            p = p.next

        slow = fast = head
        for i in range(k % length):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = head
        head = slow.next
        slow.next = None

        return head
