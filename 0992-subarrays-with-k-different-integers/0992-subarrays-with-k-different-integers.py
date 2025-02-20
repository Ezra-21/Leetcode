class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def calculate(k):
            hashh = {}
            ans = 0
            j = 0
            for i in range(len(nums)):
                hashh[nums[i]] = hashh.get(nums[i],0)+1
                while len(hashh)>k:
                    hashh[nums[j]]-=1
                    if hashh[nums[j]]==0:
                        del hashh[nums[j]]
                    j+=1
                ans += (i-j+1)
            return ans
        return calculate(k)-calculate(k-1)


        