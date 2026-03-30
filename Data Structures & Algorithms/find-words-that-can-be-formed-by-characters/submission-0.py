class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = defaultdict(int)
        res = 0

        for char in chars:
            counter[char] += 1
        
        for word in words:
            counter2 = defaultdict(int)
            for ch in word:
                counter2[ch] += 1
            
            for k, value in counter2.items():
                if not(k in counter and value <= counter[k]):
                    break
            else:
                res += len(word)
        
        return res
