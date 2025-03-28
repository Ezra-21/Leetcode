class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn = nums[0]
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>=minn:
                left = mid+1
            else:
                minn = min(minn,nums[mid])
                right = mid-1

        return minn