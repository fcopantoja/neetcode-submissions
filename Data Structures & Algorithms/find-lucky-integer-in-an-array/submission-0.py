class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1
        
        max_count = float("-inf")
        lucky_number = -1

        for k, v in counts.items():
            if v > max_count and k == v:
                max_count = v
                lucky_number = k
        
        return lucky_number