class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p
        if remainder == 0:
            return 0

        def solve(remainder,nums):
            prefic_dic = {0:-1}
            prefix = 0
            min_len = len(nums)
            for i , val in enumerate(nums):
                prefix += val
                ok = (prefix - remainder ) % remainder
                if ok in prefic_dic:
                    min_len =  min(min_len,i-prefic_dic[ok])
                
                prefic_dic[prefix%remainder] = i
            return min_len
        ans = solve(remainder,nums)
        return ans if ans < len(nums) else -1
                