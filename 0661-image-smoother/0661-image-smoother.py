class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row,col = len(img),len(img[0])
        smooth_img =[[0]*col for _ in range(row)] 

        for i in range(row):
            for j in range(col):
                summ = 0
                num = 0
                for r in range(i-1,i+2):
                    for c in range(j-1,j+2):
                        if r>=0 and r<row and c>=0 and c<col:
                            summ+=img[r][c]
                            num+=1
                smooth_img[i][j] = summ//num

        return smooth_img
        