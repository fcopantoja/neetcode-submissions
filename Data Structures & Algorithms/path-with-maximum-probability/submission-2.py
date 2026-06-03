class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {i: [] for i in range(n)}

        for edge, prob in zip(edges, succProb):
            graph[edge[0]].append((edge[1], prob))
            graph[edge[1]].append((edge[0], prob))

        max_heap = [(-1, start_node)]
        visited = set()

        while max_heap:
            prob, node = heapq.heappop(max_heap)
            prob = -prob

            if node == end_node:
                return prob

            if node in visited:
                continue
            
            visited.add(node)      

            for nei, neiprob in graph[node]:
                if nei not in visited:
                    heapq.heappush(max_heap, (-(prob * neiprob), nei))
        
        return 0
        