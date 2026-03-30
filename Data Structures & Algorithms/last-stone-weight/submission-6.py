class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        count = 0
        
        while len(stones) > 1:
            first = heapq.heappop_max(stones)
            second = heapq.heappop_max(stones)
            
            if second < first:
                heapq.heappush_max(stones, first - second)
            
            print(stones)
            #count += 1
            #if count > 18:
            #    break
            #print(stones)

        
        return stones[0] if stones else 0
