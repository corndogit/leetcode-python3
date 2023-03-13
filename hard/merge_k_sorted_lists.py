import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None  # no linked lists were provided

        heap = []

        def next_node_val():
            while len(heap) > 0:
                yield heapq.heappop(heap)

        for ll in lists:
            while ll is not None:
                heapq.heappush(heap, ll.val)
                ll = ll.next

        if len(heap) == 0:
            return None  # only empty linked lists were provided

        head = ListNode(next(next_node_val()))
        tail = head
        for n in next_node_val():
            tail.next = ListNode(n)
            tail = tail.next
        return head
