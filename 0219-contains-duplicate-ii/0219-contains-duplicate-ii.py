class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashh = {}  # Dictionary to store the last seen index of each number

        for i in range(len(nums)):
            if nums[i] in hashh:
                # Check if the difference between indices is less than or equal to k
                if i - hashh[nums[i]] <= k:
                    return True
            
            # Update the hash with the current index
            hashh[nums[i]] = i

        return False
