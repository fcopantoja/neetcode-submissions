# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        cur = head
        previous = dummy

        while cur:
            if cur.val == val:
                next_node = cur.next
                previous.next = next_node
            else:
                previous = cur
            cur = cur.next

        return dummy.next