class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtracking(i, path, total):
            if i == len(nums):
                print(path, total)
                nonlocal res
                res += total
                return
            
            # Include number
            path.append(nums[i])
            backtracking(i + 1, path, total ^ nums[i])
            path.pop()

            # Do not include number
            backtracking(i + 1, path, total)
            
        backtracking(0, [], 0)
        
        return res
        

