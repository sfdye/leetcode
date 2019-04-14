# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(li.val, i) for i, li in enumerate(lists) if li]
        heapq.heapify(heap)
        head = cur = ListNode(0)
        while heap:
            val, i = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        return head.next

