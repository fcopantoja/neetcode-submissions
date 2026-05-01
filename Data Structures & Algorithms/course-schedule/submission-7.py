class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])

        def dfs(node): # this DFS checks if graph has cycle
            if states[node] == VISITED:
                return False
            if states[node] == VISITING:
                return True
            
            states[node] = VISITING
            for nei in graph[node]:
                if dfs(nei):
                    return True

            states[node] = VISITED
            return False

        for course in range(numCourses):
            if dfs(course):
                return False
    
        return True

    
    def canFinishK(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        

