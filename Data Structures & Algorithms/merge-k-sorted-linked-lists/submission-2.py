# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeLists(self, l1: ListNode, l2: ListNode):
        dummy = ListNode(-1)
        head = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        
        if l1:
            dummy.next = l1
        else:
            dummy.next = l2
        
        return head.next
            


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None
        
        for lst in lists:
            result = self.mergeLists(result, lst)

        return result

        