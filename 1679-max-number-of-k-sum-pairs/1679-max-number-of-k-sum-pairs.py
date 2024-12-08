
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashh = {}
        seen = set()
        for val in nums:
            if val not in hashh:
                hashh[val] = 0
            hashh[val] += 1
        ans = 0
        for num in nums:
            target = k-num
            if target not in seen and target in hashh:
                if target==num:
                    ans += hashh[target]//2
                else:
                    ans += min(hashh[num],hashh[target])
                seen.add(num)
                seen.add(target)
        return ans
        
        
        