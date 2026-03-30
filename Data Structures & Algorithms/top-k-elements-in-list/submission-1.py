from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        aux = [[] for x in range(len(nums) + 1)]

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for key, value in counter.items():
            aux[value].append(key)

        result = []
        for i in range(len(aux) - 1, 0, -1):
            while aux[i]:
                result.append(aux[i].pop())
                if len(result) == k:
                    return result

        return result
