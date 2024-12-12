class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in check:
                    return False
                if board[i][j] != '.':
                    check.add(board[i][j])   
            check1 = set()
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in check1:
                    return False
                if board[j][i] != '.':
                    check1.add(board[j][i])    


        

        for i in range(0,9,3):
            for j in range(0,9,3):
                check2 = set()
                for m in range(i,i+3):
                    for n in range(j,j+3):
                        if board[m][n] != '.' and board[m][n] in check2:
                            return False
                        if board[m][n] != '.':
                            check2.add(board[m][n])   

                

        return True  


