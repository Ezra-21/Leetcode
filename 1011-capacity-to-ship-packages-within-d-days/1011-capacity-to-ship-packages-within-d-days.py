class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right = max(weights),sum(weights)
        ans = right
        while left<=right:
            weight = (left+right)//2
            summ,count = 0,0
            for i,val in enumerate(weights):
                summ+=val
                if summ>weight:
                    count+=1
                    summ = val
                if i==len(weights)-1:
                    count+=1
                
            if count <= days:
                ans = weight
                right = weight-1 
            else:
                left = weight+1
        return ans
            
                


