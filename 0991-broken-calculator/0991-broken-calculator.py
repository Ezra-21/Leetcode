class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        while startValue!=target:
            if target > startValue:
                if target%2==0:
                    target//=2
                else:
                    target+=1
                count+=1
            else:
                count+=(startValue-target)
                break
        return count