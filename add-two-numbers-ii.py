# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2, s3 = [], [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        s = 0
        while s1 or s2:
            if s1:
                s += s1.pop()
            if s2:
                s += s2.pop()
            s3.append(s % 10)
            s = s // 10
        if s:
            s3.append(s)
        head = ListNode(0)
        node = head
        while s3:
            node.next = ListNode(s3.pop())
            node = node.next
        return head.next
