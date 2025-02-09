class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        new_mat = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_mat[j][i] = matrix[i][j]

        for row in new_mat:
            row.reverse()

        for i in range(n):
            for j in range(n):
                matrix[i][j] = new_mat[i][j]