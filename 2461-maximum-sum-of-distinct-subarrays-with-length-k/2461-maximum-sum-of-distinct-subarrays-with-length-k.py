class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        i,j = 0,0
        check = set()
        summ = 0
        while j<len(nums):
            if nums[j] not in check:
                check.add(nums[j])
                summ += nums[j]
                if j-i+1 == k:
                    max_sum = max(summ,max_sum)
                    summ -= nums[i]
                    check.remove(nums[i])
                    i+=1
                j+=1
            else:
                while nums[i] != nums[j]:
                    check.remove(nums[i])
                    summ -= nums[i]
                    i+=1
                check.remove(nums[i])
                summ -= nums[i]
                i+=1
                
        return max_sum
            

        