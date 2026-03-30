class Solution:
    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = set()
        adj = {i: [] for i in range(numCourses)}

        for pre in prerequisites:
            adj[pre[0]].append(pre[1])

        def dfs(node):
            print(visited, node)
            if node in visited:
                return False
            
            if adj[node] == []:
                return True
            
            visited.add(node)
            for nei in adj[node]:
                res = dfs(nei)
                if not res: return False
            visited.remove(node)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
    
        return True

    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {x: [] for x in range(numCourses)}
        queue = deque()

        for n1, n2 in prerequisites:
            graph[n2].append(n1)

        # Topological Sort, Kahn algorithm
        indegree = [0] * numCourses

        for i in range(numCourses):
            for j in graph[i]:
                indegree[j] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        
        count = 0
        while queue:
            node = queue.popleft()
            count += 1

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return count == numCourses

        

