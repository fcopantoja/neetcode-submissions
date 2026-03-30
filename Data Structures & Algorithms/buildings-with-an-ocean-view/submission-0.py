class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for idx, height in enumerate(heights):
            while stack and stack[-1][0] <= height:
                stack.pop()
            stack.append((height, idx))
        
        
        return [x[1] for x in stack]
