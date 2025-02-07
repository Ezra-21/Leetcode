class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,7,3):
            
            for j in range(0,7,3):
                sett = set()
                for r in range(0+i,3+i):
                    for c in range(0+j,3+j):
                        if board[r][c].isdigit():
                            if board[r][c] not in sett:
                                sett.add(board[r][c])
                            else:
                                return False
        for i in range(9):
            sett1 = set()
            sett2 = set()
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] not in sett1:
                        sett1.add(board[i][j])
                    else:
                        return False
                if board[j][i].isdigit():
                    if board[j][i] not in sett2:
                        sett2.add(board[j][i])
                    else:
                        return False

        return True
