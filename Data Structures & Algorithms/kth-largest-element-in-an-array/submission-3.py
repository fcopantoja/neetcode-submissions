class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) >= k and num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
            elif len(heap) < k:
                heapq.heappush(heap, num)
        print(heap)
        return heap[0]
        