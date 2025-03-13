class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1]]
        for i in range(rowIndex):
            temp = [0] + pascal[-1] + [0]
            row = []
            for j in range(len(pascal[-1])+1):
                row.append(temp[j] + temp[j+1])   
            pascal.append(row)
            
        return pascal[-1]