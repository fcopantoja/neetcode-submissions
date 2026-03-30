class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for i in range(n)]
        col_set = set()
        pos_diag = set()
        neg_diag = set()

        def backtracking(row):
            if row == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for col in range(n):
                if col in col_set or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                
                col_set.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = "Q"

                backtracking(row + 1)

                col_set.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = "."
        
        backtracking(0)
        return result
