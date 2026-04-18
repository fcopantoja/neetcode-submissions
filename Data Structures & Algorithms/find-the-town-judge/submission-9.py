class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = {x: [] for x in range(1, n + 1)}
        indegree = [0] * n

        for t in trust:
            adj[t[0]].append(t[1])

        for i in range(1, n + 1):
            for node in adj[i]:
                indegree[i - 1] += 1
        
        
        candidate = None
        for i in range(n):
            if indegree[i] == 0:
                candidate = i + 1

        if candidate:
            for k, v in adj.items():
                if k == candidate:
                    continue
                
                if candidate not in v:
                    return -1
        
        return candidate or -1
        
        