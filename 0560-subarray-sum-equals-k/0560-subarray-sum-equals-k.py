class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        prefix_sums = {
            0: 1
        }
        
        for n in nums:
            running_sum += n
            target = running_sum - k
            count += prefix_sums.get(target, 0)
            prefix_sums[running_sum] = prefix_sums.get(running_sum, 0) + 1

        return count