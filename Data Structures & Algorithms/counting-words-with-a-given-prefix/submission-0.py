class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            is_prefix = True
            for i in range(len(pref)):
                if pref[i] != word[i]:
                    is_prefix = False
                    break
            if is_prefix:
                count += 1
            
        return count