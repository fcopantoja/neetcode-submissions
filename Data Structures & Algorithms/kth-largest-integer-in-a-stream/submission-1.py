import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-x for x in nums]
        heapq.heapify(nums)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val * -1)
        return heapq.nsmallest(self.k, self.heap)[self.k - 1] * -1
        

        
