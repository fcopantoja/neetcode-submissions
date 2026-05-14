class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        graph = {i: [] for i in range(n)}
        visited = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)



        def bfs(node):
            queue = deque([node])

            while queue:
                node = queue.popleft()
                visited.add(node)

                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(node)

        for node in range(n):
            if node not in visited:
                bfs(node)
                count += 1


        return count