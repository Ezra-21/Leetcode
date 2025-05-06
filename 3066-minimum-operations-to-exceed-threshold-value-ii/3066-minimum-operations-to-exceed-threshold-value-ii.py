class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)
        while nums[0]<k and len(nums)>=2:
            count += 1
            a,b = heapq.heappop(nums),heapq.heappop(nums)
            heapq.heappush(nums,a*2+b)
        return count
