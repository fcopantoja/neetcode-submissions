class Solution:
    def isAnagramNaive(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = defaultdict(int)

        for ch in s:
            counts[ch] += 1
        
        for ch in t:
            counts[ch] -= 1
            if counts[ch] < 0:
                return False
        
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = [0] * 26
        counter2 = [0] * 26

        for ch in s:
            counter1[ord(ch) - ord('a')] += 1
        
        for ch in t:
            counter2[ord(ch) - ord('a')] += 1
        return counter1 == counter2

        