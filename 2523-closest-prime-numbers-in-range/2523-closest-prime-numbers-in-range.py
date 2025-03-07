class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        arr = [0]*(right+1)
        arr[1] = -1
        for i in range(2,right+1):
            if arr[i]==0:
                j = i*i
                while j<right+1:
                    arr[j] = -1
                    j+=i
        
        collect = []
        for num in range(left,right+1):
            if arr[num]==0:
                collect.append(num)

        Minn = float('inf')
        hashh = {}
        for i in range(len(collect)-1):
            diff = collect[i+1]-collect[i]
            if Minn>diff:
                Minn = diff
                hashh[Minn] = [collect[i],collect[i+1]]

        return hashh[Minn] if Minn!=float('inf') else [-1,-1]

        