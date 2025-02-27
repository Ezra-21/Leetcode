class Solution:
    def matrixBlockSum(self, matrix: List[List[int]], k: int) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        c_m = [[0]*(col+1) for _ in range(row+1)] 
        for r in range(1,row+1):
            for c in range(1,col+1):
                c_m[r][c] = c_m[r-1][c]+c_m[r][c-1]+matrix[r-1][c-1]-c_m[r-1][c-1]

        ans = [[0]* col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                row1 = max(0,i-k)
                col1 = max(0,j-k)
                row2 = min(row-1,i+k)
                col2 = min(col-1,j+k)
                result = c_m[row2+1][col2+1]-c_m[row2+1][col1]-c_m[row1][col2+1]+c_m[row1][col1]
                ans[i][j] = result
                
        return ans


        