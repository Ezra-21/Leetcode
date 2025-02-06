class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def make_colmn(i,j,matrix):
            for j in range(len(matrix[0])):
                if matrix[i][j]!=0:
                    matrix[i][j] = ''
        def make_row(i,j,matrix):
            for i in range(len(matrix)):
                if matrix[i][j]!=0:
                    matrix[i][j] = ''

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    make_colmn(i,j,matrix)
                    make_row(i,j,matrix)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='':
                    matrix[i][j] = 0

