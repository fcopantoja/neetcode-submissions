class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = float("-inf")
        min_even = float("inf")
        counts = defaultdict(int)

        for ch in s:
            counts[ch] += 1
        
        for v in counts.values():
            if v % 2 == 0:
                min_even = min(min_even, v)
            else:
                max_odd = max(max_odd, v)
        
        print(max_odd, min_even)

        return max_odd - min_even

        
