class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashh = {0:-1}
        summ = 0
        for i in range(len(nums)):
            summ+=nums[i]
            remain = summ%k
            if remain in hashh and i-hashh[remain]>1:
                return True
            if remain not in hashh:
                hashh[remain] = i

        return False
        