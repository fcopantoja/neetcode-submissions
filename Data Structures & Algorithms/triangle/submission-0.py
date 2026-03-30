class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        matrix = [[0] * (len(triangle[-1]) + 1) for _ in range(len(triangle) + 1)]
        rows = len(matrix)
        cols = len(matrix[0])

        level = 0
        
        for row in range(rows - 2, -1, -1): 
            for col in range(cols - 2 - level, -1, -1):
                print(row, col)
                matrix[row][col] = triangle[row][col] + min(matrix[row + 1][col], matrix[row + 1][col + 1])
            
            level += 1
            
        return matrix[0][0]
