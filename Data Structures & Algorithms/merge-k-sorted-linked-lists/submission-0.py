# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = []
        for i in range(len(lists)):
            tmp = lists[i]
            while tmp:
                result.append(tmp.val)
                tmp = tmp.next
        print(result)
        heapq.heapify(result)
        print(result)
        dummy = ListNode()
        head = dummy

        while result:
            cur = heapq.heappop(result)
            dummy.next = ListNode(cur)
            dummy = dummy.next
        
        return head.next
        