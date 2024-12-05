
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_hash = {0:1}
        prefix = 0
        number_of_subarray = 0
        for i in range(len(nums)):
            prefix += nums[i]
            
            if prefix-k in prefix_hash:
                number_of_subarray += prefix_hash[prefix-k]
            
            if prefix not in prefix_hash:
                prefix_hash[prefix] = 0
            prefix_hash[prefix] += 1
            
                
        return number_of_subarray
