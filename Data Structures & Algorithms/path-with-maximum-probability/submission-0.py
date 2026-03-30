import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for edge, prob in zip(edges, succProb):
            graph[edge[0]].append((edge[1], prob))
            graph[edge[1]].append((edge[0], prob))

        print(graph)
        max_heap = []
        heapq.heappush(max_heap, (1, start_node))
        visited = set()
        
        while max_heap:
            prob, node = heapq.heappop(max_heap)
            visited.add(node)

            if node == end_node:
                return -prob

            for nei, probnei in graph[node]:
                if nei not in visited:
                    heapq.heappush(max_heap, (-1 * abs(probnei * prob), nei))

        return 0  

                



