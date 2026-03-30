class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # converto max heap
        self.k = k
        self.nums = nums
        heapq.heapify_max(self.nums)
        
        

    def add(self, val: int) -> int:
        heapq.heappush_max(self.nums, val)
        kth_largest = heapq.nlargest(self.k, self.nums)
        return kth_largest[-1]

        
