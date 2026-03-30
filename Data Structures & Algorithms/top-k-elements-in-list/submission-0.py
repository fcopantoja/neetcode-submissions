from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        arr = []
        for key, val in counter.items():
            arr.append((key, val))
        arr = sorted(arr, key = lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(arr[i][0])
        return result
