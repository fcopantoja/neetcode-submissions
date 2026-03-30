class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = []

        def backtracking(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0

            
            a = backtracking(i + 1, total + nums[i])
            b = backtracking(i + 1, total - nums[i])

            return a + b


        
        res = backtracking(0, 0)
        return res