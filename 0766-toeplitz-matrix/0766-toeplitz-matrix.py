class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        Min = min(len(matrix),len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                l,r = i,j
                check = matrix[i][j]
                while l<len(matrix) and r<len(matrix[0]):
                    if check != matrix[l][r]:
                        return False
                    l+=1
                    r+=1

        return True
