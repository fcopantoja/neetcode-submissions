class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        row_set = [set() for x in range(rows)]
        col_set = [set() for x in range(cols)]
        matrix_set = defaultdict(set)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == ".":
                    continue
                print(row, col, (row // 3) + (col // 3))
                if (
                    board[row][col] in row_set[row] or
                    board[row][col] in col_set[col] or 
                    board[row][col] in matrix_set[row // 3, col // 3]
                ):
                    return False
                
                row_set[row].add(board[row][col])
                col_set[col].add(board[row][col])
                matrix_set[row // 3, col // 3].add(board[row][col])
            
        return True