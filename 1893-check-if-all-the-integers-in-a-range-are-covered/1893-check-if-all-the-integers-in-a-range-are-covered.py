class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right+1):
            for start,end in ranges:
                if start <= i <= end:
                    break
            else:
                return False
        return True


                


                    
                
