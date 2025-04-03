class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashh = Counter(nums)
        arr = []
        for val,fre in hashh.items():
            arr.append([fre,val])
        arr.sort(reverse=True)
        ans = [val for fre,val in arr[:k]]
        return ans