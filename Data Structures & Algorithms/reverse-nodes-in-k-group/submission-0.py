# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy

        while True:
            kthNode = self.getKNode(groupPrev, k)
            if not kthNode:
                break

            groupNext = kthNode.next
            previous = kthNode.next
            current = groupPrev.next
            
            while current != groupNext:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            
            tmp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tmp

        return dummy.next
            
    
    def getKNode(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        
        return current