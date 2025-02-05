class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        summ = 0
        for num in nums:
            if num % 2 == 0:
                summ+=num
        for val,idx in queries:
            if nums[idx]%2==0:
                summ -= nums[idx]
            nums[idx] += val
            if nums[idx] %2 == 0:
                summ+=nums[idx]
            
            ans.append(summ)

        return ans

        