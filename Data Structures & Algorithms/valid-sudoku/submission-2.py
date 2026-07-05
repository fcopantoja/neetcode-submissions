class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        rows_set = [set() for _ in range(rows)]
        cols_set = [set() for _ in range(cols)]
        matrix_set = defaultdict(set)

        for row in range(rows):
            for col in range(cols):
                
                num = board[row][col]
                if num == ".":
                    continue

                if (
                    num in rows_set[row] or
                    num in cols_set[col] or
                    num in matrix_set[(row // 3, col // 3)]
                ):
                    return False
                
                rows_set[row].add(num)
                cols_set[col].add(num)
                matrix_set[(row // 3, col // 3)].add(num)

                
        
        return True