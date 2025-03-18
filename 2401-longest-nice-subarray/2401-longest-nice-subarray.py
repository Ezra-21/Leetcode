class Solution:
    def expand(self,check,binary):
        for i,val in enumerate(binary):
            val = int(val)
            if check[i]&val:
                return False
        for i,val in enumerate(binary):
            val = int(val)
            check[i]+=val
        return True

    def shrink(self,check,binary):
        for i,val in enumerate(binary):
            val = int(val)
            check[i]-=val
                
            
    def longestNiceSubarray(self, nums: List[int]) -> int:
        check = [0]*30
        ans = 1
        j = 0
        for i,num in enumerate(nums):
            binary = format(num,'030b')
            while not self.expand(check,binary):
                binn = format(nums[j],'030b')
                self.shrink(check,binn)
                j+=1

            ans = max(ans,i-j+1)

        return ans
            
