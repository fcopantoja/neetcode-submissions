class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()

        def bfs(r, c):
            queue = deque([(r, c)])
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            while queue:
                r1, c1 = queue.popleft()
                for direction in directions:
                    r2 = r1 + direction[0]
                    c2 = c1 + direction[1]

                    if (
                        c2 in range(cols) and
                        r2 in range(rows) and
                        grid[r2][c2] == "1" and
                        (r2, c2) not in visited
                    ):
                        queue.append((r2, c2))
                        visited.add((r2, c2))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        
        return islands

