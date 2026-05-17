class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        result = []
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtracking(i, path):
            if i == len(digits):
                result.append("".join(path[:]))
                return
            
            for ch in hashmap[digits[i]]:
                path.append(ch)
                backtracking(i + 1, path)
                path.pop()
        
        backtracking(0, [])
        print(result)
        return result

