class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        def sort_array(arr):
            
            maxi = max(arr)
            place = 1

            

            while maxi//place:
                bucket = [[] for _ in range(10)]
                for num in arr:
                    idx = (num//place)%10
                    bucket[idx].append(num)
                
                arr.clear()

                for elements in bucket:
                    arr.extend(elements)

                place*=10
            
            return arr

        n = len(nums)
        nums = sort_array(nums)
        gap = 0
        for i in range(n-1):
            gap = max(gap,nums[i+1]-nums[i])

        return gap
            
                

                



        