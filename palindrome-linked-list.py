class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        # by the time fast reaches the end, slow will be in the middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        p = slow.next
        last = None
        while p:
            next = p.next
            p.next = last
            last = p
            p = next

        p1, p2 = last, head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next

        return p1 is None
