class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        sett = set(allowed)
        count = 0
        for word in words:
            for ch in word:
                if ch not in sett:
                    break
            else:
                count += 1
        
        return count
