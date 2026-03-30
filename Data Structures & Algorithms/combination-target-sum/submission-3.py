class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(i, total, path):
            if total == target:
                result.append(path[:])
                return
            
            if total > target or i >= len(nums):
                return

            # Do not include number
            backtracking(i + 1, total, path)
            
            # Include number
            path.append(nums[i])
            backtracking(i, total + nums[i], path)
            path.pop()

        backtracking(0, 0, [])
        return result


