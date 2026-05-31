class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            w = (r - l)
            h = min(heights[l], heights[r])
            area = h * w

            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
    
        return res
        
