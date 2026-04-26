class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0

        for i in range(n):
            height = heights[i]

            right_most = i + 1

            while right_most < n and heights[right_most] >= height:
                right_most += 1
            
            left_most = i

            while left_most >= 0 and heights[left_most] >= height:
                left_most -= 1
            
            right_most -= 1
            left_most += 1

            max_area = max(max_area, height * (right_most - left_most + 1))
        
        return max_area
