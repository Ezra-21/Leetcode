class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_0 = 0
        ans = []
        total = 1
        for num in nums:
            if count_0>1:
                break
            if num==0:
                count_0+=1
                continue
            total *= num


        for num in nums:
            if count_0==0:
                ans.append(total//num)   
                continue
            elif count_0==1:
                if num==0:
                    ans.append(total)
                    continue

            ans.append(0)
        return ans