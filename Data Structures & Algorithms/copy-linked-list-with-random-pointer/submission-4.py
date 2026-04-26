"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {}
        cur = head
        dummy = Node(-1)
        head_dummy = dummy

        while cur:
            new_node = Node(cur.val)
            seen[cur] = new_node
            dummy.next = new_node
            cur = cur.next
            dummy = dummy.next

        cur = head
        dummy = head_dummy.next
        while cur:
            if cur.random:
                dummy.random = seen[cur.random]
            cur = cur.next
            dummy = dummy.next

        return head_dummy.next


    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_mapping = {}
        curr = head

        while curr:
            old_mapping[curr] = Node(curr.val)
            curr = curr.next

        for old, new in old_mapping.items():
            new.next = old_mapping.get(old.next)
            new.random = old_mapping.get(old.random)
        
        return old_mapping.get(head)




















