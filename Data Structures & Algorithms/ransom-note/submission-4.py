
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_arr = [0] * 26
        magazine_arr = [0] * 26

        for ch in ransomNote:
            ransom_arr[ord(ch) - ord("a")] += 1
        
        for ch in magazine:
            ransom_arr[ord(ch) - ord("a")] -= 1
        
        for item in ransom_arr:
            if item > 0:
                return False
        return True