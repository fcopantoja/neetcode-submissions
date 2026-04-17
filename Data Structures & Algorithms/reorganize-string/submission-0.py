from collections import defaultdict
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = defaultdict(int)
        max_heap = []

        for ch in s:
            counter[ch] += 1

        max_heap = [(-v, k) for k, v in counter.items()]
        heapq.heapify(max_heap)
        res = ""
        prev = None

        while max_heap or prev:
            if prev and not max_heap:
                return ""
            cnt, char = heapq.heappop(max_heap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if cnt != 0:
                prev = (cnt, char)

        return res