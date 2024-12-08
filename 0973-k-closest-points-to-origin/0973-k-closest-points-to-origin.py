class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for x1,x2 in points:
            result = x1**2 + x2**2
            arr.append([result,[x1,x2]])

        arr.sort()
        ans = []
        for i in range(k):
            ans.append(arr[i][1])

        return ans
        