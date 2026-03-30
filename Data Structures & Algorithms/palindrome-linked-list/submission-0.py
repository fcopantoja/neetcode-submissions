# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        word = []

        curr = head

        while curr:
            word.append(curr.val)
            curr = curr.next
        
        l, r = 0, len(word) - 1

        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        
        return True