class NumArray:

    def __init__(self, nums: List[int]):
        self.cumm = [0]
        for i in range(len(nums)):
            self.cumm.append(self.cumm[i]+nums[i])
        
    def sumRange(self, left: int, right: int) -> int:
        return self.cumm[right+1] - self.cumm[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)