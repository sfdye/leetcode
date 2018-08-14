class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        l = []
        node = head
        while node:
            l.append(node.val)
            node = node.next

        l.sort()

        dummy = ListNode(0)
        p = dummy
        for x in l:
            q = ListNode(x)
            p.next = q
            p = q

        return dummy.next
