class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashh = {}
        for val in nums:
            if val not in hashh:
                hashh[val] = 0
            hashh[val] += 1

        arr = []
        for num,fre in hashh.items():
            arr.append([fre,num])
        
        arr.sort(reverse=True)

        ans = []
        for i in range(k):
            ans.append(arr[i][1])

        return ans


        