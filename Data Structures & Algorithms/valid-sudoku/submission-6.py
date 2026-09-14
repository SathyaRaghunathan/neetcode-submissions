class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        three = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                #check for .
                if board[i][j] == ".":
                    continue
                #check rows
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])
                #check cols
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].add(board[i][j])
                #check 3x3
                if board[i][j] in three[ (i//3,j//3) ]:
                    return False
                else:
                    three[(i//3,j//3)].add(board[i][j])
        return True
