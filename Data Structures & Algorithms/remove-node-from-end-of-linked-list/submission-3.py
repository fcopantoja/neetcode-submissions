# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
        """
        length = 0
        tmp = head

        while tmp:
            length += 1
            tmp = tmp.next

        if length - n == 0:
            return head.next

        current = head
        for i in range(1, length - n):
            current = current.next

        current.next = current.next.next
        return head
        """

        