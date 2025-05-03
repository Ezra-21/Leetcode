class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse = True)
        self.arr = []
        for i in range(min(k,len(nums))):
            self.arr.append(nums[i])
        heapq.heapify(self.arr)
        self.k = k

            


    def add(self, val: int) -> int:
        heapq.heappush(self.arr,val)
        if len(self.arr)>self.k:
            heapq.heappop(self.arr)
        return self.arr[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)