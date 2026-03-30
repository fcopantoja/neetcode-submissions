class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = set()
        adj = {i: [] for i in range(numCourses)}

        for pre in prerequisites:
            adj[pre[0]].append(pre[1])

        def dfs(node):
            print(visited)
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

        

