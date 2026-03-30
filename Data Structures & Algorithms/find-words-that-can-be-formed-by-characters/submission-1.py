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
                print(counter2)
                if ch not in counter or counter2[ch] > counter[ch]:
                    is_good = False
                    break
            
            if is_good:
                print(word)
                res += len(word)
        
        return res
