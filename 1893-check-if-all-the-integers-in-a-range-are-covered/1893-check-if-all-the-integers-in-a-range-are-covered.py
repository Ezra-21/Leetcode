class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        
        for i in range(left,right+1):
            for s,e in ranges:
                if s<=i<=e:
                    return True
                    
        return False
                 
