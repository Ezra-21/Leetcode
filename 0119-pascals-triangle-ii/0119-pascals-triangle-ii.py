class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[0,1,0]]
        for _ in range(rowIndex):
            temp,use = [0],ans[-1]
            for i in range(1,len(use)):
                temp.append(use[i-1]+use[i])
            temp.append(0)
            ans.append(temp)

        return ans[-1][1:-1]

