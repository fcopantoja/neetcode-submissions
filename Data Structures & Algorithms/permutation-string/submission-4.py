class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        counter1 = [0] * 26
        counter2 = [0] * 26

        for ch in s1:
            counter1[ord(ch) - ord('a')] += 1
        
        l, r = 0, 0

        while r < len(s2):
            counter2[ord(s2[r]) - ord('a')] += 1

            while (r - l + 1) > k:
                counter2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            
            if counter1 == counter2:
                return True
            
            r += 1
        
        return False
