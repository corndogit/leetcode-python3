# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Stack solution"""
        if not head:
            return

        stack = []
        while head is not None:
            stack.append(head.val)
            head = head.next

        def pop_stack():
            while len(stack) > 0:
                yield stack.pop()

        new_head = ListNode(next(pop_stack()))
        new_tail = new_head

        for p in pop_stack():
            new_tail.next = ListNode(p)
            new_tail = new_tail.next

        return new_head
