# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def find_number(linkedlist):
            """Traverses a given linked list with nodes containing digits 0-9 and returns its (reversed) integer form"""
            current = linkedlist
            number = []
            while current.val is not None:
                number.append(str(current.val))
                current = current.next
                if current is None:
                    return int(''.join(list(reversed(number))))
            return 0

        # create a new linked list from digits in the result
        result = [int(digit) for digit in str(find_number(l1) + find_number(l2))]
        new_linkedlist = ListNode(result.pop())
        if len(result) <= 0:
            return new_linkedlist

        new_linkedlist.next = ListNode(result.pop())
        head = new_linkedlist.next

        while len(result) > 0:
            head.next = ListNode(result.pop())
            head = head.next

        return new_linkedlist
