class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        col = [0]*len(matrix[0])
        row = [0]*len(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    col[j] = 1
                    row[i] = 1

        for i in range(len(col)):
            if col[i] == 1:
                for j in range(len(matrix)):
                    matrix[j][i] = 0

        for i in range(len(row)):
            if row[i] == 1:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        return matrix
            
        