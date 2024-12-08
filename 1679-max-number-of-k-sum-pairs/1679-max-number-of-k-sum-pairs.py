class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashh = Counter(nums)
        ans = 0
        
        for num in list(hashh.keys()):
            target = k - num
            if target in hashh:
                if num == target:
                    # If the number and its complement are the same
                    ans += hashh[num] // 2
                else:
                    # Count the minimum pairs between `num` and `target`
                    ans += min(hashh[num], hashh[target])
                # Decrement counts to avoid double-counting
                hashh[target] = max(0, hashh[target] - hashh[num])
                hashh[num] = 0

        return ans
