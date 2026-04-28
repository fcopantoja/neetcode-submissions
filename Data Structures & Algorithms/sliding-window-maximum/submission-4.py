from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_heap = []
        result = []

        for i in range(len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))

            while (i + 1) > k and max_heap[0][1] <= (i - k):
                heapq.heappop(max_heap)

            if (i + 1) >= k:
                result.append(max_heap[0][0] * -1)

        print(result)
        return result