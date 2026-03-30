class Solution:
    def bfs(self, grid, r, c):
        print(r, c)
        visited = set()
        queue = deque([(r, c, [(r, c)])])
        directions = [[0, 1], [1,0], [-1, 0], [0, -1]]

        while queue:
            r1, c1, path = queue.popleft()
            visited.add((r1, c1))
            
            if grid[r1][c1] == 0:
                grid[path[0][0]][path[0][1]] = len(path) - 1
                return

            for direction in directions:
                r2 = r1 + direction[0]
                c2 = c1 + direction[1]

                if (
                    r2 in range(len(grid)) and
                    c2 in range(len(grid[0])) and
                    (r2, c2) not in visited and
                    grid[r2][c2] != -1
                ):
                    queue.append((r2, c2, path + [(r2, c2)]))
        


    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                val = grid[r][c]
                if val not in [0,-1]:
                    self.bfs(grid, r, c)
        
        
