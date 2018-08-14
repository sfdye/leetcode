class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size = 0
        l = []
        node = head
        while node:
            l.append(node)
            size += 1
            node = node.next

        if n == size:
            return head.next

        node = l[size - n - 1]
        node.next = node.next.next

        return head
