class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(int)
        permutations = []
        result = []

        for num in nums:
            counts[num] += 1
        
        def dfs():
            if len(permutations) == len(nums):
                result.append(permutations[:])
                return
            
            for n in counts.keys():
                if counts[n] > 0:
                    counts[n] -= 1
                    permutations.append(n)
                    dfs()
                    counts[n] += 1
                    permutations.pop()
        
        dfs()
        return result