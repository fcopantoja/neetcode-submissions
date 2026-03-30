class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort() # We sort because line 23 does a whileloop and scan sequentially until new number comes in
        result = []

        def backtracking(i, total, path):
            if total == target:
                result.append(path[:])
                return
            
            if total > target or i == len(nums):
                return
            
            # Include number
            path.append(nums[i])
            backtracking(i + 1, total + nums[i], path)
            path.pop()

            # Do not include number
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1 # Increment i until different number is found
            
            backtracking(i + 1, total, path)

        backtracking(0, 0, [])
        return result

    