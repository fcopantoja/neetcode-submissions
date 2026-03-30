class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, total, path):
            if total == target:
                result.append(path.copy())
                return
            elif total > target or i == len(nums):
                return
            
            dfs(i + 1, total, path)
            path.append(nums[i])
            dfs(i, total + nums[i], path)
            path.pop()
        
        dfs(0, 0, [])

        return result


