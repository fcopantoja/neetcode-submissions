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

        def backtrcaking(i, curr_str):
            if len(curr_str) == len(digits):
                result.append(curr_str)
                return
            
            for ch in hashmap[digits[i]]:
                backtrcaking(i + 1, curr_str + ch)

        backtrcaking(0, "")
        return result