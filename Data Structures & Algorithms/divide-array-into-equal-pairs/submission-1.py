class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
        
        for k, v in counter.items():
            if v % 2 == 1:
                return False
        
        return True