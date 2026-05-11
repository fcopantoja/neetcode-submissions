class Solution:
    def setZeroesExtraSpace(self, matrix: List[List[int]]) -> None:
        row_zeros = [0] * len(matrix) 
        col_zeros = [0] * len(matrix[0]) 

        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_zeros[i] = True
                    col_zeros[j] = True
        

        for i in range(n):
            for j in range(m):
                if row_zeros[i] or col_zeros[j]:
                    matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        row_zeroes = [False] * rows 
        col_zeroes = [False] * cols

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    row_zeroes[row] = True
                    col_zeroes[col] = True
        
        for row in range(rows):
            for col in range(cols):
                if row_zeroes[row] or col_zeroes[col]:
                    matrix[row][col] = 0
        

