class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(openP, closedP, path):
            if closedP == openP == n:
                res.append("".join(path))
                return

            if openP < n:
                path.append("(")
                backtracking(openP + 1, closedP, path)
                path.pop()
            
            if closedP < openP:
                path.append(")")
                backtracking(openP, closedP + 1, path)
                path.pop()
        
        backtracking(0, 0, [])
        return res
        
            

            
