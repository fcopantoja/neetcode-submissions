class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zeros = [0] * len(matrix) 
        col_zeros = [0] * len(matrix[0]) 

        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_zeros[i] = True
                    col_zeros[j] = True

        print(row_zeros)
        print(col_zeros)
        

        for i in range(n):
            for j in range(m):
                if row_zeros[i] or col_zeros[j]:
                    matrix[i][j] = 0
        
