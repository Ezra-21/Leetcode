class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j,ans = 0,0,0
        while j < len(nums):
            if nums[j]==0:
                if k == 0:
                    while nums[i] != 0:
                        i+=1
                    i+=1
                    k+=1
                else:
                    j+=1
                    k -= 1
            else:
                j+=1
            ans = max(j-i,ans)
        return ans
                
        