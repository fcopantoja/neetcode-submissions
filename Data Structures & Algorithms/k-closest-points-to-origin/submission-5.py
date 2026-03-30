from math import sqrt

class Solution:
    def get_distance(self, x: int, y: int):
        return sqrt(x ** 2 + y ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
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
    
    def kClosestNaive(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for point in points:
            distance = self.get_distance(point[0], point[1])
            heapq.heappush(hp, (distance, point))
        
        result = []

        for i in range(k):
            result.append(heapq.heappop(hp)[1])
        
        return result
        