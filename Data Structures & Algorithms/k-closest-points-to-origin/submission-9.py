class Solution:
    """def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = x ** 2 + y ** 2
            heap.append((distance, [x, y]))
        
        heapq.heapify(heap)
        res = []
        for i in range(k):
            d, point = heapq.heappop(heap)
            res.append(point)
        
        return res"""

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            distance = x ** 2 + y ** 2
            heapq.heappush(max_heap, (-distance, [x, y]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        res = []
        while max_heap:
            d, point = heapq.heappop(max_heap)
            res.append(point)
        
        return res
            
