# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dq = deque()
        current = head

        while current is not None:
            dq.append(current)
            current = current.next


        take_in_front = True
        dummy = ListNode(0)
        tail = dummy

        while dq:
            if take_in_front:
                tail.next = dq.popleft()
            else:
                tail.next = dq.pop()
            
            tail = tail.next
            take_in_front = not take_in_front

        
        tail.next = None

        