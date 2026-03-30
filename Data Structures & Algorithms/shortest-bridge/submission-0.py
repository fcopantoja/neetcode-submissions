class Solution:
    def get_first_cell(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return row, col

    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = set()
        level = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(r, c):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                grid[r][c] == 0
                    
            ):
                return

            visited.add((r, c))
            queue.append((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        r, c = self.get_first_cell(grid)
        dfs(r, c)

        while queue:
            n = len(queue)
            for _ in range(n):
                r, c = queue.popleft()

                for direction in directions:
                    r2, c2 = r + direction[0], c + direction[1]

                    if (
                            r2 in range(rows) and
                            c2 in range(cols) and
                            (r2, c2) not in visited
                    ):
                        if grid[r2][c2] == 1:
                            return level

                        queue.append((r2, c2))
                        visited.add((r2, c2))

            level += 1
        
        return -1