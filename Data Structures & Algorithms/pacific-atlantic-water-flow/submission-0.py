class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific_set = set()
        atlantic_set = set()

        def dfs(r, c, visited, previousHeight):
            if (
                r not in range(rows) or
                c not in range(cols) or
                heights[r][c] < previousHeight or
                (r, c) in visited
            ):
                return

            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

            
        # Pacific
        for col in range(cols):
            dfs(0, col, pacific_set, 0)
        
        for row in range(rows):
            dfs(row, 0, pacific_set, 0)

        for col in range(cols):
            dfs(rows - 1, col, atlantic_set, 0)
        
        for row in range(rows):
            dfs(row, cols - 1, atlantic_set, 0)


        return list(pacific_set & atlantic_set)

        
        



        