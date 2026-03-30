class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0, 1], [1,0], [-1,0], [0, -1]]
        queue = deque()
        fresh = 0
        minutes = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                    
                if grid[row][col] == 2:
                    queue.append((row, col))
    
        while queue and fresh > 0:
            for i in range(len(queue)):
                node = queue.popleft()
                for direction in directions:
                    dr = node[0] + direction[0]
                    dc = node[1] + direction[1]

                    if (
                        0 <= dr < rows and
                        0 <= dc < cols and
                        grid[dr][dc] == 1
                    ):
                        fresh -= 1
                        queue.append((dr, dc))
                        grid[dr][dc] = 2
            minutes += 1             


        return minutes if fresh == 0 else -1
          