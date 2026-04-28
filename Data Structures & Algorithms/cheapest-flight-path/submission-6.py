import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {x: [] for x in range(n)}
        min_heap = []

        for src2, dest, price in flights:
            graph[src2].append((price, dest))

        heapq.heappush(min_heap, (0, src, 0))
        visited = set()


        while min_heap:
            cost, node, stops = heapq.heappop(min_heap)
            visited.add(node)
            if node == dst:
                return cost

            for nei in graph[node]:
                nei_price, nei_dest = nei
                if nei_dest not in visited and stops <= k:
                    heapq.heappush(min_heap, (cost + nei_price, nei_dest, stops + 1))

        return -1