class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        rows = {}
        boxes = {}

        for r in range(len(board[0])):
            for c in range(len(board)):
                if board[r][c] == '.':
                    return False
                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if (r//3, c//3) not in boxes:
                    boxes[(r//3,c//3)] = set()
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[(r//3,c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r//3,c//3)].add(board[r][c])
        
        return True