class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        graph = {x: [] for x in range(numCourses)}
        indegree = [0] * numCourses

        for n1, n2 in prerequisites:
            graph[n2].append(n1)

        for i in range(numCourses):
            for j in graph[i]:
                indegree[j] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        visited = set()
        res = []
        print(queue)
        while queue:
            node = queue.popleft()
            if node in visited:
                return []

            res.append(node)
            visited.add(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return res if len(res) == numCourses else []

        

