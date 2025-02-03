class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        count = 0
        for i in range(left,right+1):
            
            for s,e in ranges:
                if s<=i<=e:
                    count +=1
                    break
            else:
                return False
                    
        return count == right-left+1
                 
