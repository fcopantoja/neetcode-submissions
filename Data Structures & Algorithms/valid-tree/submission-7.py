from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False
        
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        queue = deque([(0, -1)]) # first node, dummy parent
        visited = set()

        while queue:
            node, parent = queue.popleft()

            if node in visited:
                return False

            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue
                
                if nei not in visited:
                    queue.append((nei, node))
                    

        return len(visited) == n


    