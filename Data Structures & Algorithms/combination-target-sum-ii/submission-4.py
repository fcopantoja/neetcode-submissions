class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort() # We sort because line 23 does a whileloop and scan sequentially until new number comes in
        result = []

        def backtracking(i, total, path):
            if total == target:
                result.append(path.copy())
                return
            
            if total > target or i >= len(nums):
                return
            
            path.append(nums[i])
            backtracking(i + 1, total + nums[i], path)
            path.pop()

            while (i < len(nums) - 1) and nums[i] == nums[i + 1]:
                i += 1

            backtracking(i + 1, total, path)
            
        backtracking(0, 0, [])
        return result

    