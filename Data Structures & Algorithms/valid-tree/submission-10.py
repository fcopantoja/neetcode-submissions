class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False
        
        graph = {i: [] for i in range(n)}

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        print(graph)
        queue = deque([(0, -1)])
        visited = set()
        visited.add(0)

        while queue:
            node, parent = queue.popleft()
            
            for nei in graph[node]:
                if nei == parent:
                    continue
            
                if nei in visited:
                    return False

                queue.append((nei, node))
                visited.add(nei)
        
        return len(visited) == n

        

    