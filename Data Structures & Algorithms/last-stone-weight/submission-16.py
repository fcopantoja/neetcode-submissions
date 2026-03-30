class Solution:
    def lastStoneWeightWithMaxHeap(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            
            if second < first:
                heapq.heappush_max(stones, first - second)
            
        
        return stones[0] if stones else 0

    
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            if second > first:
                heapq.heappush(stones, (second - first) * -1)
            
        
        return abs(stones[0]) if stones else 0



    def lastStoneWeight(self, stones: List[int]) -> int:
        print(stones)
        stones = [-x for x in stones]
        heapq.heapify(stones)


        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)

            if stone1 > stone2:
                heapq.heappush(stones, (stone1 - stone2) * -1)
        
        return abs(stones[0]) if stones else 0
                





























