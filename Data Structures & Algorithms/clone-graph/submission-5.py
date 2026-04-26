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
        old_mapping = dict()
        visited = set()

        while queue:
            old_node = queue.popleft()
            old_mapping[old_node] = Node(old_node.val)

            for nei in old_node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
        
        for old, new in old_mapping.items():
            for nei in old.neighbors:
                new.neighbors.append(old_mapping.get(nei))
        
        return old_mapping.get(node)


        


    def cloneGraphDFS(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_mapping = {}
        visited = set()
        head = node

        def dfs(node):
            if not node:
                return
            
            new_node = Node(val=node.val)
            old_mapping[node] = new_node

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        dfs(node)

        for old, new in old_mapping.items():
            for nei in old.neighbors:
                new.neighbors.append(old_mapping[nei])
        
        return old_mapping[head]

        
        
        