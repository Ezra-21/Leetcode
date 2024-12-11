class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr1= []
        ans = []
        for num in arr:
            arr1.append((abs(num-x),num))

        arr1.sort(key=lambda x:(x[0],x[1]))

        for i in range(k):
            ans.append(arr1[i][1])
        ans.sort()
        return ans
        


        