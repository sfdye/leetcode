class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        d = {}
        node = head
        while node != None:
            if node in d:
                return True
            d[node] = 1
            node = node.next
        return False
