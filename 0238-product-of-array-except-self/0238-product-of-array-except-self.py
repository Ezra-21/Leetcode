class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1

        temp = 0
        index = -1

        for i , val in enumerate(nums):
            suffix *= val

            if val == 0:
                temp = 1
                index = i

            if i<len(nums)-1:
                temp *= nums[i+1]

        hashh = {index:temp}
        ans = []
        for i , val in enumerate(nums):
            if i>0 :
                prefix *= nums[i-1]
            
            if val!=0:
                suffix//=val
            else:
                if i in hashh:
                    suffix = hashh[i]
                else:
                    suffix = 0

            ans.append(prefix*suffix)

        return ans


        

        