import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((t, v))
        visited = set()
        heap = [(0, k)]
        t = 0

        while heap:
            t1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, t1)

            for node in graph[n1]:
                t2, n2 = node
                if n2 not in visited:
                    heapq.heappush(heap, (t1 + t2, n2))
        
        print(visited)
        return t if len(visited) == n else -1




