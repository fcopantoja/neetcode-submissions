
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)

        def backtracking(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                visited[i] = True
                path.append(nums[i])
                backtracking(path)
                path.pop()
                visited[i] = False

        backtracking([])
        return res
