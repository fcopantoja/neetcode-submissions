class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    r2 = r + dr
                    c2 = c + dc

                    if (
                        0 <= r2 < rows and
                        0 <= c2 < cols and
                        grid[r2][c2] == "1" and
                        (r2, c2) not in visited
                    ):
                        queue.append((r2, c2))
                        visited.add((r2, c2))

        
        res = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    res += 1
        
        return res
