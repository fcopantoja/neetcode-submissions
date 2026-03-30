class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        res = 0

        for val in counts.values():
            if val == 1:
                return -1
            res += math.ceil(val / 3)
        
        return res
