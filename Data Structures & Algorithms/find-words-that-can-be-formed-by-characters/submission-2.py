class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = defaultdict(int)
        res = 0

        for char in chars:
            counter[char] += 1
        
        for word in words:
            counter2 = defaultdict(int)
            is_good = True
            for ch in word:
                counter2[ch] += 1
                if counter2[ch] > counter[ch]:
                    is_good = False
                    break
            
            if is_good:
                res += len(word)
        
        return res
