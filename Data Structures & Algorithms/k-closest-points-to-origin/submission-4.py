from math import sqrt

class Solution:
    def get_distance(self, x: int, y: int):
        return sqrt(x ** 2 + y ** 2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for point in points:
            distance = self.get_distance(point[0], point[1])
            heapq.heappush(hp, (distance, point))
        
        result = []

        for i in range(k):
            result.append(heapq.heappop(hp)[1])
        
        return result
        