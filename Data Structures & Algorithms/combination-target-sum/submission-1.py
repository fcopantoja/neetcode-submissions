class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(curr_sum, path, i):
            if curr_sum == target:
                result.append(path.copy())
            elif curr_sum > target:
                return
            
            for i in range(i, len(nums)):
                path.append(nums[i])
                dfs(curr_sum + nums[i], path, i)
                path.pop()
        
        dfs(0, [], 0)

        return result


