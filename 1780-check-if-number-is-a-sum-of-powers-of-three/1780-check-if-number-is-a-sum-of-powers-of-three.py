class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        arr = []
        m = int(math.pow(n,1/3))+1
        for i in range(m):
            b=math.pow(3,i)
            arr.append(b)
        for i in range(len(arr)-1,-1,-1):
            if n>=arr[i]:
                n-=arr[i]
            print(n)
        
        return n==0


        
        