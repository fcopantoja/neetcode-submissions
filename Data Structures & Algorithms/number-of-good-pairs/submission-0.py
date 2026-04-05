class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        counter = defaultdict(int)

        for num in nums:
            res += counter[num]
            counter[num] += 1
        
        return res