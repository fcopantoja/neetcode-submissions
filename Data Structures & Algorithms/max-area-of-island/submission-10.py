class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        areas = []
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def bfs(r: int, c: int):
            queue = deque([(r, c)])
            directions = [[0,1], [1,0], [-1, 0], [0, -1]]
            area = 1
            while queue:
                r1, c1 = queue.popleft()
                visited.add((r1, c1))
                for direction in directions:
                    r2 = r1 + direction[0]
                    c2 = c1 + direction[1]
                    if (
                        r2 in range(rows) and
                        c2 in range(cols) and
                        grid[r2][c2] == 1 and
                        (r2, c2) not in visited
                    ):
                        print((r2, c2))
                        area += 1
                        queue.append((r2, c2))
                        visited.add((r2, c2))
            
            areas.append(area)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    bfs(row, col)
        
        #print(areas)
        return max(areas) if areas else 0