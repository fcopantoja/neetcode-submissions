class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        result = 0

        while right < len(s):
            print(s[left:right], result)
            char_map = defaultdict(int)
            max_ocurrence = 0
            length = right - left + 1
            for i in range(left, right + 1):
                char_map[s[i]] += 1
                max_ocurrence = max(max_ocurrence, char_map[s[i]])
            print(char_map)
            if length - max_ocurrence <= k:
                result = max(result, length)
                right += 1
            else:
                left += 1

            
        
        return result

