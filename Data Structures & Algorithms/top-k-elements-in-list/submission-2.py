from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        ocurrences = [(value * -1, key) for key, value in counter.items()]
        heapq.heapify(ocurrences)

        result = []
        for i in range(k):
            result.append(heapq.heappop(ocurrences)[1])

        return result