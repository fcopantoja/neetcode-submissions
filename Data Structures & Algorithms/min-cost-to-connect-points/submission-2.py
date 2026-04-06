import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i: [] for i in range(len(points))}
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                distance = abs(x2 - x1) + abs(y2 - y1)
                graph[i].append((distance, j))
                graph[j].append((distance, i))
                    

        min_heap = [(0, 0)]
        visited = set()
        res = 0

        while min_heap:
            cost, n = heapq.heappop(min_heap)

            if len(visited) == len(points):
                break
            
            if n in visited:
                continue
            
            res += cost
            visited.add(n)

            for cost_nei, nei in graph[n]:
                if nei not in visited:
                    heapq.heappush(min_heap, (cost_nei, nei))
        
        return res


