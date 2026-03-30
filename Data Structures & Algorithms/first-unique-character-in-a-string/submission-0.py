
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for idx, ch in enumerate(s):
            if ch in counter:
                counter[ch]["counter"] += 1
                counter[ch]["indexes"].append(idx)
            elif ch not in counter:
                counter[ch] = {"counter": 1, "indexes": [idx]}

        
        for k, v in counter.items():
            if len(counter[k]["indexes"]) == 1:
                return counter[k]["indexes"][0]
        
        return -1

        