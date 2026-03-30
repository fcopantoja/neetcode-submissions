class Solution:

    def checkValidString(self, s: str) -> bool:
        res = []
        memo = {}

        def dfs(i, openP) -> bool:
            if openP < 0:
                return False
            if i == len(s):
                return openP == 0

            if (i, openP) in memo:
                return memo[(i, openP)]
                    
            if s[i] == "*":
                result = (
                    dfs(i + 1, openP + 1) or 
                    dfs(i + 1, openP - 1) or 
                    dfs(i + 1, openP)
                )
            else:
                if s[i] == "(":
                    result = dfs(i + 1, openP + 1)
                if s[i] == ")":
                    result = dfs(i + 1, openP - 1)
          
            memo[(i, openP)] = result
            return result
        
        return dfs(0, 0)
        