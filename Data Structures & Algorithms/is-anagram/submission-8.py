class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
       return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bools:
        arr1 = [0] * 26
        arr2 = [0] * 26

        for ch in s:
            arr1[ord(ch) - ord('a')] += 1
        
        for ch in t:
            arr2[ord(ch) - ord('a')] += 1
        
        return arr1 == arr2
        