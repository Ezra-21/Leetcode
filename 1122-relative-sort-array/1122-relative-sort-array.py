class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashh = {}
        for num in arr1:
            if num not in hashh:
                hashh[num] = 0
            hashh[num]+=1
        ans = []
        for num in arr2:
            for _ in range(hashh[num]):
                ans.append(num)
            del hashh[num]
        
        if len(hashh):
            temp = []
            for val,fre in hashh.items():
                for _ in range(fre):
                    temp.append(val)
            temp.sort()
            ans.extend(temp)

        return ans
        