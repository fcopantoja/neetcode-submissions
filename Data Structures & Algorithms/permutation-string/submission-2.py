class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        left = 0
        counter = [0] * 26
        counter2 = [0] * 26
        for ch in s1:
            counter[ord(ch) - ord("a")] += 1

        for right in range(len(s2)):
            ch = s2[right]
            counter2[ord(ch) - ord("a")] += 1
            
            if right - left + 1 > k:
                counter2[ord(s2[left]) - ord("a")] -= 1
                left += 1

            if counter == counter2:
                return True
        
        return False
        