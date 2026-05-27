class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = 0
            res = 1

            while queue:
                r, c  = queue.popleft()
                
                for dr, dc in directions:
                    r2, c2 = r + dr, c + dc
                    if (
                        0 <= r2 < rows and
                        0 <= c2 < cols and
                        grid[r2][c2] == 1
                    ):
                        queue.append((r2, c2))
                        grid[r2][c2] = 0
                        res += 1

            return res
        
        area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = max(area, bfs(row, col))
        
        return area


