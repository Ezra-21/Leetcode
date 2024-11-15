class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        new = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                summ,count = 0,0
                
                for r in range(i-1,i+2):
                    for c in range(j-1,j+2):
                        if (r>=0 and c>=0 and r<=row-1 and c<=col-1):
                            count+=1
                            summ+=img[r][c]
                
                new[i][j] = summ//count
        return new
