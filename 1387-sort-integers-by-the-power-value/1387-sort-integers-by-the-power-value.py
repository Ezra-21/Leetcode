class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def operation(num):
            count = 0
            while num != 1:
                count+=1
                if num%2==1:
                    num = 3*num+1
                else:
                    num //= 2
            return count

        arr = []

        for i in range(lo,hi+1):
            arr.append([operation(i),i])

        
        arr.sort()

        
        return arr[k-1][1]



            
            
        