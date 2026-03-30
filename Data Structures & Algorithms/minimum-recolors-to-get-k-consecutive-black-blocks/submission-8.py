class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = k
        result = float("inf")

        while right <= len(blocks):
            counter = {"W": 0, "B": 0}
            for i in range(left, right):
                counter[blocks[i]] += 1
            if counter["W"] <= k:            
                result = min(result, counter["W"])
            left += 1
            right += 1
        
        return result

