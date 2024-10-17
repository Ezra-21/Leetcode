class Solution:
    def minimumSteps(self, s: str) -> int:
        arr = list(s)
        count = 0
        left = arr.index('1')
        for right in range(left+1,len(s)):
            if arr[right] == '0':
                arr[right],arr[left] = arr[left],arr[right]
                count+=1
                left+=1
        return count
                
            
            
        