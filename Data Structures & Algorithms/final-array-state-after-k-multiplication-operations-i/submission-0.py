class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = [(x, idx) for idx, x in enumerate(nums)]
        heapq.heapify(min_heap)
        print(min_heap)
        print(nums)
        for i in range(k):
            val, idx = heapq.heappop(min_heap)
            new_val = val * multiplier
            heapq.heappush(min_heap, (new_val, idx))
            nums[idx] = new_val
        print(nums)
        return nums
        