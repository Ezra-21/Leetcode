class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row,col = len(matrix),len(matrix[0])
        transpose = [[0]* row for _ in range(col)]
        for c in range(col):
            for r in range(row):
                transpose[c][r] = matrix[r][c]

        return transpose        