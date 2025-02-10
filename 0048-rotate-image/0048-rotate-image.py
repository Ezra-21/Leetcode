class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        arr = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                arr[j][(n-1)-i] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = arr[i][j]