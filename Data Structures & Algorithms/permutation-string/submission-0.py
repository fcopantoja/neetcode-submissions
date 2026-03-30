class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        left = 0
        counter = defaultdict(int)
        for ch in s1:
            counter[ch] += 1

        for right in range(k, len(s2) + 1):
            counter2 = defaultdict(int)
            for i in range(left, right):
                counter2[s2[i]] += 1
                if counter == counter2:
                    print(counter2, counter)
                    return True

            left += 1
        
        return False
        