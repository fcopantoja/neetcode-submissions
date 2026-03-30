class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left = [-1] * n
        for i in range(n):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1][1]
            
            stack.append((heights[i], i))

        stack = []
        right = [n] * n

        for i in range(n - 1, -1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1][1]
            
            stack.append((heights[i], i))
        
        res = float("-inf")
        for i in range(n):
            w = right[i] - left[i] - 1
            h = heights[i]
            res = max(res, w * h)

        return res