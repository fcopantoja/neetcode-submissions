# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        n = 0

        while curr:
            n += 1
            if not curr.next:
                break
            curr = curr.next

        curr.next = head
        k = k % n
        print(k)
        for i in range(n - k):
            curr = curr.next
        
        next = curr.next
        curr.next = None
        
        return next

        

        

