class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        j=[]
        for item in range(1,n+1):
            j.append(item)
        i=0
        while len(j)!=1:
            l=len(j)
            remover=i+k-1
            j.remove(j[remover%l])
            i=remover%l

        return(j[0])

##### TIME COMPLEXITY O(n)
##### SPACE COMPLETY O(1)