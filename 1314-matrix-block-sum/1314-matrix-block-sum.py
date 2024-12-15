class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row,col = len(mat),len(mat[0])
        prefixSum = [[0]*(col+1) for _ in range(row+1)]

        for i in range(row):
            for j in range(col):
                prefixSum[i+1][j+1] = prefixSum[i][j+1]+prefixSum[i+1][j]-prefixSum[i][j]+mat[i][j]

        new_mat = [[0]*(col) for _ in range(row)]

        for i in range(row):
            for j in range(col):
                r1,c1 = max(0,i-k) , max(0,j-k)
                r2,c2 = min(row-1,i+k),min((col-1,j+k))

                summ = prefixSum[r2+1][c2+1]-prefixSum[r2+1][c1]-prefixSum[r1][c2+1]+prefixSum[r1][c1]
                new_mat[i][j] = summ

        return new_mat

        