class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        indegree = [[0] * COLS for _ in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                for dr, dc in directions:
                    r2 = dr + row
                    c2 = dc + col

                    if (
                        0 <= r2 < ROWS and
                        0 <= c2 < COLS and
                        matrix[r2][c2] < matrix[row][col]
                    ):
                        indegree[row][col] += 1
        
        queue = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if indegree[row][col] == 0:
                    queue.append((row, col))

    
        lis = 0

        while queue:
            for _ in range(len(queue)):
                r, c  = queue.popleft()
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if (0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]):
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            queue.append((nr, nc))
            
            lis += 1


        return lis


