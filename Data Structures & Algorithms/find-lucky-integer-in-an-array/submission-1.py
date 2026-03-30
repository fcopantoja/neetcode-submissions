class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = defaultdict(int)

        for num in arr:
            counts[num] += 1

        res = -1

        for k, v in counts.items():
            if k == v:
                res = max(res, k)
        
        return res