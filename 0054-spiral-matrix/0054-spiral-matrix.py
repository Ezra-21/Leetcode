class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row , col = len(matrix),len(matrix[0])
        check = row*col
        top,bottom,right,left = 0,len(matrix)-1,len(matrix[0])-1,0
        count = 0
        ans = []
        while left<=right and top<=bottom:
            temp_left,temp_top,temp_right,temp_bottom = left,top,right,bottom
            while left<=right:
                ans.append(matrix[top][left])
                left+=1
            top+=1
            while top<=bottom:
                ans.append(matrix[top][right])
                top+=1
            right-=1
            while temp_top+1<=bottom and right>=temp_left:
                ans.append(matrix[bottom][right])
                right-=1
            bottom-=1
            while bottom>temp_top and temp_left<=temp_right-1:
                ans.append(matrix[bottom][temp_left])
                bottom-=1
            left,top = temp_left+1,temp_top+1
            right,bottom = temp_right-1,temp_bottom-1


        return(ans)
            


            
        