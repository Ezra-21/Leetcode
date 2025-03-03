class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        num_less = 0
        num_equal = 0
        for num in nums:
            if num<pivot:
                num_less+=1
            elif num==pivot:
                num_equal+=1
        
        ans = [0]*(num_less+num_equal)
        idx_less,idx_equal = 0,num_less
        for num in nums:
            if num<pivot:
                ans[idx_less] = num
                idx_less+=1
            elif num==pivot:
                ans[idx_equal] = num
                idx_equal+=1
            else:
                ans.append(num)


        return ans


        