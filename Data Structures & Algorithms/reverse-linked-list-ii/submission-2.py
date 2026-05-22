# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev_group = dummy
        last = dummy
        
        for i in range(left - 1):
            prev_group = prev_group.next
        
        first = prev_group.next
        
        for i in range(right):
            last = last.next
        
        
        prev_group.next = last
        next_node = last.next

        # reverse group
        prev = next_node
        curr = first

        while curr and curr != next_node:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        

      
        return dummy.next
