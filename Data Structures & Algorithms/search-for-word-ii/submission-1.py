class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False
    
    def __repr__(self) -> str:
        return str(self.children)
    
    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.add_word(word)

        rows = len(board)
        cols = len(board[0])
        visited = set()
        result = set()

        def backtracking(r, c, node, word):
            if (
                r < 0 or r == rows or 
                c < 0 or c == cols or
                board[r][c] not in node.children or
                (r, c) in visited
            ):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                result.add(word)

            backtracking(r + 1, c, node, word)
            backtracking(r - 1, c, node, word)
            backtracking(r, c + 1, node, word)
            backtracking(r, c - 1, node, word)

            visited.remove((r, c))


        for row in range(rows):
            for col in range(cols):
                backtracking(row, col, root, "")

        return list(result)
            