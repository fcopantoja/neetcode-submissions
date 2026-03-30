
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(path):
            print(path)
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for n in nums:
                if n in path:
                    continue
                
                path.append(n)
                dfs(path)
                path.pop()

        dfs([])
        return res
