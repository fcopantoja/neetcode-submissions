class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        result = [0] * len(heights)
        stack = []

        for i in range(len(heights)):
            while stack and heights[i] > heights[stack[-1]]:
                j = stack.pop()
                result[j] += 1
            if stack:
                result[stack[-1]] += 1
            stack.append(i)
        
        return result