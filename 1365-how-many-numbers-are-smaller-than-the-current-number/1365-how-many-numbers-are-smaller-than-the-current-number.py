class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = nums.copy()
        temp.sort()
        hashh = {}
        for i,num in enumerate(temp):
            if num not in hashh:
                hashh[num] = i

        ans = []
        for val in nums:
            ans.append(hashh[val])

        return ans
            
        