class Solution:
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c) -> int:
            result = 0
            queue = deque([(r, c)])
            while queue:
                node = queue.popleft()
                visited.add(node)

                for d in directions:
                    r0 = node[0] + d[0]
                    c0 = node[1] + d[1]
                    
                    if (
                        r0 in range(rows) and
                        c0 in range(cols) and
                        grid[r0][c0] == 0
                    ):
                        result += 1
                    if (
                        r0 not in range(rows) or 
                        c0 not in range(cols)
                    ):
                        result += 1

                for direction in directions:
                    r2 = node[0] + direction[0]
                    c2 = node[1] + direction[1]
                    
                    if (
                        r2 in range(rows) and
                        c2 in range(cols) and
                        (r2, c2) not in visited and
                        grid[r2][c2] == 1
                    ):
                        visited.add((r2, c2))
                        queue.append((r2, c2))


            return result
        
        perimeter = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    perimeter = bfs(row, col)
        return perimeter
        

        