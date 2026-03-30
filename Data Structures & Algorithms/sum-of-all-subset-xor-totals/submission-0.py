class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = []
        res = 0

        def backtracking(i, path, total):
            if i == len(nums):
                print(path, total)
                nonlocal res
                res += total
                result.append(path.copy())
                return
            
            # Include number
            path.append(nums[i])
            backtracking(i + 1, path, total ^ nums[i])
            path.pop()

            # Do not include number
            backtracking(i + 1, path, total)
            
        backtracking(0, [], 0)
        
        print(result, res)

        return res
        

