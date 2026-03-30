import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for i, j, c in flights:
            graph[i].append((c, j))
        
        min_heap = [(0, src, 0)]
        visited = set()

        while min_heap:
            cost, node, stops = heapq.heappop(min_heap)
            visited.add(node)
            
            if node == dst:
                return cost

            for nei_cost, nei in graph[node]:
                if nei not in visited:
                    if stops <= k:
                        heapq.heappush(min_heap, (nei_cost + cost, nei, stops + 1))
            
    
        return -1