class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = defaultdict(int)
        res = 0

        for char in chars:
            counter[char] += 1
        
        for word in words:
            word_counter = defaultdict(int)
            is_good = True
            for ch in word:
                word_counter[ch] += 1
                if word_counter[ch] > counter[ch]:
                    is_good = False
                    break
            
            if is_good:
                res += len(word)
        
        return res
