class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target>1 and maxDoubles>0:
            if target%2==1:
                target-=1
            else:
                target//=2
                maxDoubles-=1
            count+=1
        if target>1:
            count += target-1

        return count
