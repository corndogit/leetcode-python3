import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: ListNode):
        self.ll = head
        self.all = []
        while head is not None:
            self.all.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        if len(self.all) == 1:
            return self.all[0]
        return random.choice(self.all)
