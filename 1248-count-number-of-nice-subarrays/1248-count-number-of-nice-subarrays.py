class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        store = []
        index = 0
        count_odd = start = ans = 0

        j = 0
        for i in range(len(nums)):
            if nums[i] %2 ==1:
                store.append(i)
                count_odd += 1
            
            while count_odd > k:
                if nums[j] %2 ==1:
                    index += 1
                    count_odd -= 1
                
                j += 1
                start = j
            
            if count_odd == k:
                ans += (store[index]-start+1)

        return ans

                
