class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left,right = 0,len(matrix)-1
        while left<right:
            top,bottom = left,right
            for i in range(right-left):
                temp1 = matrix[top+i][right]
                matrix[top+i][right] = matrix[top][left+i]
                temp2 = matrix[bottom][right-i]
                matrix[bottom][right-i] = temp1
                temp1 = matrix[bottom-i][left]
                matrix[bottom-i][left] = temp2
                matrix[top][left+i] = temp1
            
            right-=1
            left+=1

        return matrix



        