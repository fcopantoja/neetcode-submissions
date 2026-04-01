import math
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) ** 2
        counts = {x:0 for x in range(1, n + 1)}
        rows = len(grid)
        cols = len(grid[0])
        a = None

        for row in range(rows):
            for col in range(cols):
                counts[grid[row][col]] += 1
                if counts[grid[row][col]] > 1:
                    a = grid[row][col]
        
        for k, v in counts.items():
            if not v:
                b = k
        
        return [a, b]


        



                
        