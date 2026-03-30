"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        queue = deque([root])

        while queue:
            queue_copy = queue.copy()
            n = len(queue)
            print(n, queue_copy)
            for i in range(n):
                node = queue.popleft()
                if n > 1 and i < n - 1:
                    node.next = queue_copy[i + 1]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root
            