from _heapq import heapify
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        l = 0
        r = len(nums) - 1
        res = float("-inf")

        while l < r:
            res = max(res, nums[l] + nums[r])
            l += 1
            r -= 1

        
        return res
