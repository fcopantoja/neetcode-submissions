from collections import defaultdict
import heapq

class Solution:
    def topKFrequentNaiveHeap(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        ocurrences = [(value * -1, key) for key, value in counter.items()]
        heapq.heapify(ocurrences)

        result = []
        for i in range(k):
            result.append(heapq.heappop(ocurrences)[1])

        return result

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counter.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for j in range(len(buckets[i])):
                result.append(buckets[i][j])
                if len(result) == k:
                    return result
    
        return result

        
        









