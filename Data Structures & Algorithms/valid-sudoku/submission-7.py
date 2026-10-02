class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        tbyt = defaultdict(set)

        for r in range(9):
            for c in range(9):
                #check for .
                if board[r][c] == ".":
                    continue
                #check if in rows
                if board[r][c] in rows[r]:
                    return False
                else:
                    rows[r].add(board[r][c])
                #check if in cols
                if board[r][c] in cols[c]:
                    return False
                else:
                    cols[c].add(board[r][c])
                #check for 9by9
                if board[r][c] in tbyt[(r//3,c//3)]:
                    return False
                else:
                    tbyt[(r//3,c//3)].add(board[r][c])
        return True