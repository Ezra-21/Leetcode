class Solution:
    def clearDigits(self, s: str) -> str:
        check = ('1','2','3','4','5','6','7','8','9','0')
        arr= list(s)
        i = 0
        while i<len(arr):
            if arr[i] in check:
                if i==0:
                    arr.pop(i)
                else:
                    arr.pop(i)
                    i-=1
                    arr.pop(i)
                continue
            i+=1

        return ''.join(arr)                
