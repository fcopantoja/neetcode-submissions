
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = defaultdict(int)

        for ch in s:
            counter[ch] += 1
        
        print(counter)

        for i, ch in enumerate(s):
            if counter[ch] == 1:
                return i
        
        return -1
