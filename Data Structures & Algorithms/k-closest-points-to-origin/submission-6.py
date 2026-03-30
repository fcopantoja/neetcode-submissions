from math import sqrt

class Solution:

    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            distance = x ** 2 + y ** 2
            min_heap.append([distance, x, y])
        
        heapq.heapify(min_heap)
        result = []
        for i in range(k):
            distance, x, y = heapq.heappop(min_heap)
            result.append([x,y])
        
        return result
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:k]
    
        