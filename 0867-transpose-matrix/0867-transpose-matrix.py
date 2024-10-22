class Solution:
    def transpose(self,    arr: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        transpose_matrix = [[0]*row for _ in range(col)] 
        for i in range(col):
            for j in range(row):
                transpose_matrix[i][j] = matrix[j][i]
        return transpose_matrix