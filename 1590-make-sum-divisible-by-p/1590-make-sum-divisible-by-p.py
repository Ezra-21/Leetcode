class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p
        if remainder == 0:
            return 0

        def solve(remainder,nums):
            prefix_dic = {0:-1}
            prefix = 0
            min_len = len(nums)
            for i , val in enumerate(nums):
                prefix += val
                target_remainder = (prefix%p - remainder ) % p
                if target_remainder in prefix_dic:
                    min_len =  min(min_len,i-prefix_dic[target_remainder])
                
                prefix_dic[prefix%p] = i
            return min_len
        ans = solve(remainder,nums)
        return ans if ans < len(nums) else -1
                