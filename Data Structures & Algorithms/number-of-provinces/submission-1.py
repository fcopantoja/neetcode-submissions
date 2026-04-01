class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = {x:[] for x in range(n)}  
        cols = len(isConnected)
        rows = len(isConnected[0])
        visited = set()

        def bfs(node):
            queue = deque([node])
            while queue:
                node = queue.popleft()
                visited.add(node)

                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

        
        for col in range(cols):
            for row in range(rows):
                if isConnected[col][row] == 1 and row != col:
                    graph[row].append(col)
        
        
        result = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                result += 1
        
        return result
        
        

        
