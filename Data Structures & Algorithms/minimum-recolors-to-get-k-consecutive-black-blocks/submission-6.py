class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = k
        result = k + 1

        while right <= len(blocks):
            counter = {"W": 0, "B": 0}
            for i in range(left, right):
                counter[blocks[i]] += 1            
            result = min(result, counter["W"])
            left += 1
            right += 1
        
        return result

