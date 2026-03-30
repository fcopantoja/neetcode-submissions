class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(total, path, i):
            if total == target:
                result.append(path.copy())
                return
            elif total > target or i >= len(candidates):
                return            
            
            path.append(candidates[i])
            dfs(total + candidates[i], path, i + 1)
            path.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: # No entiendo esta parte
                i += 1
            dfs(total, path, i + 1)
        
        dfs(0, [], 0)

        return result

    