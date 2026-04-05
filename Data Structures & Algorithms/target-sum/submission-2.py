class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtracking(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            
            if (i, total) in dp:
                return dp[(i, total)]
            
            a = backtracking(i + 1, total + nums[i])
            b = backtracking(i + 1, total - nums[i])

            return a + b
        
        return backtracking(0, 0)