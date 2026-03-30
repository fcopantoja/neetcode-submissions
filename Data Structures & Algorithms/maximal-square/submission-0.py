class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        cache = [[0] * (cols + 1) for _ in range(rows + 1)]

        
        res = 0        
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if matrix[row][col] == "1":
                    cache[row][col] = 1 + min(cache[row + 1][col], cache[row + 1][col + 1], cache[row][col + 1])
                    res = max(res, cache[row][col])

        return res  * res