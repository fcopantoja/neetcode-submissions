class Solution:
    def is_palindrome(self, st, left, right):
        while left < right:
            if st[left] != st[right]:
                return False
            left += 1
            right -= 1
        
        return True
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtracking(i, path):
            if i >= len(s):
                result.append(path.copy())
                return
            
            for j in range(i, len(s)):
                if self.is_palindrome(s, i, j):
                    path.append(s[i:j+ 1])
                    backtracking(j + 1, path)
                    path.pop()
    
            
        backtracking(0, [])
        return result
