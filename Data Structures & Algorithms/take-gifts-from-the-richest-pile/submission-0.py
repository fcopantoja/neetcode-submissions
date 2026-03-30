import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)
        for i in range(k):
            val = -1 * heapq.heappop(max_heap)
            heapq.heappush(max_heap, -1 * math.floor(math.sqrt(val)))
        
        return sum(max_heap) * -1