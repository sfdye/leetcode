class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return head

        tmp = None

        while head != None:
            node = ListNode(head.val)
            node.next = tmp
            tmp = node
            head = head.next

        return tmp
