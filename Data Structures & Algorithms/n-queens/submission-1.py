class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        # Sets para validar conflictos en O(1)
        col_set = set()
        pos_diag = set()  # r + c
        neg_diag = set()  # r - c

        def backtracking(row):
            # Caso base: ya colocamos todas las reinas
            if row == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for col in range(n):
                # Si hay conflicto, saltamos
                if col in col_set or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                
                # Colocamos la reina
                col_set.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = "Q"

                backtracking(row + 1)

                # Backtrack: quitamos la reina
                col_set.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = "."
        
        backtracking(0)
        return result