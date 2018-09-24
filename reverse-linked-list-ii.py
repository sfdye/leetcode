class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        p = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            p = p.next
        cur = p.next
        pre = None
        for _ in range(n - m + 1):
            cur.next, pre, cur = pre, cur, cur.next
        p.next.next = cur
        p.next = pre
        return dummy.next
