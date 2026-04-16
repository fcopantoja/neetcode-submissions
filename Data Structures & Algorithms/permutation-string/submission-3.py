class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        count1 = [0] * 26
        count2 = [0] * 26

        for ch in s1:
            count1[ord(ch) - ord('a')] += 1

        left = 0
        right = 0

        while right < len(s2):
            ch = s2[right]
            count2[ord(ch) - ord('a')] += 1

            if (right - left + 1) > k:
                count2[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if count1 == count2:
                return True
            
            right += 1

        
        return False


      