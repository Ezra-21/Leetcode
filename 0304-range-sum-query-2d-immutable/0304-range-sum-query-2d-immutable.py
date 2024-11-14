class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.c_m = [[0]*(col+1) for _ in range(row+1)] #cummulative_matrix
        for r in range(1,row+1):
            for c in range(1,col+1):
                self.c_m[r][c] = self.c_m[r-1][c]+self.c_m[r][c-1]+matrix[r-1][c-1]-self.c_m[r-1][c-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.c_m[row2+1][col2+1]-self.c_m[row2+1][col1]-self.c_m[row1][col2+1]+self.c_m[row1][col1]
        return result
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)