class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        i = 0
        answer =[]
        nums = sorted(nums)
        while i<len(nums)-3:
            while i>0 and i<len(nums)-3 and nums[i] == nums[i-1]: i += 1
            j = i + 1
            k = len(nums)-2
            while j<k:
                while j>i+1 and j<len(nums)-1 and nums[j] == nums[j-1]: j += 1
                k = j + 1
                l = len(nums)-1
                while k < l:
                    value = nums[i] + nums[j] + nums[k] + nums[l]
                    if value == target:
                        answer.append([nums[i],nums[j],nums[k],nums[l]])
                        k += 1
                        while k<l and nums[k] == nums[k-1]: k += 1
                    elif value>target: l -= 1
                    else: k += 1
                j += 1

            i += 1
        return answer