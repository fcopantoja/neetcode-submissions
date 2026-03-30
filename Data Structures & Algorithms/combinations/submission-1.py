class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtracking(i, path):
            if len(path) == k:
                result.append(path[:])
                return

            
            for j in range(i, n + 1):
                path.append(j)
                backtracking(j + 1, path)
                path.pop()


        
        backtracking(1, [])
        
        return result
