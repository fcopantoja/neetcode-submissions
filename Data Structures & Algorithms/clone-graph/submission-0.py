"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        queue = deque([node])
        start = node
        visited = set()
        visited.add(node)
        oldNewMapping = {}

        while queue:
            current = queue.popleft()
            oldNewMapping[current] = Node(val=current.val)

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        for old_node, new_node in oldNewMapping.items():
            for nei in old_node.neighbors:
                new_node.neighbors.append(oldNewMapping[nei])
        
        return oldNewMapping[start]
        