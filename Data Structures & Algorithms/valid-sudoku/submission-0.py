class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row_set = collections.defaultdict(set)
        col_set = collections.defaultdict(set)
        squares_set = collections.defaultdict(set)

        for row in range(n):
            for col in range(n):
                if board[row][col] == ".":
                    continue
                if (
                    board[row][col] in row_set[row] or
                    board[row][col] in col_set[col] or
                    board[row][col] in squares_set[row // 3, col // 3]
                ):
                    return False
                
                row_set[row].add(board[row][col])
                col_set[col].add(board[row][col])
                squares_set[row // 3, col // 3].add(board[row][col])
            
        
        return True