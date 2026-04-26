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
        curr = dummy

        while dq:
            if take_in_front:
                curr.next = dq.popleft()
            else:
                curr.next = dq.pop()
            
            curr = curr.next
            take_in_front = not take_in_front

        
        curr.next = None

        