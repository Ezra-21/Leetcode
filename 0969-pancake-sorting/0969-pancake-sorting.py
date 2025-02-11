class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        maximum = len(arr)
        ans = []
        for i in range(len(arr)):
            maxi = maximum-i
            idx = arr.index(maxi)
            if idx == 0:
                arr = arr[:maxi][::-1]+arr[maxi:]
                ans.append(maxi)
            elif idx == maxi-1:
                continue
            else:
                arr = arr[:idx+1][::-1]+arr[idx+1:]
                ans.append(idx+1)
                arr = arr[:maxi][::-1]+arr[maxi:]
                ans.append(maxi)

        return ans



        