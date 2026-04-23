class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, curr_sum, path):
            if curr_sum == target:
                result.append(path[:])
                return
            
            if i >= len(nums) or curr_sum > target:
                return

            # Include same number
            path.append(nums[i])
            dfs(i, curr_sum + nums[i], path)
            path.pop()

            # Do not include number
            dfs(i + 1, curr_sum, path)
        
        dfs(0, 0, [])
        return result
