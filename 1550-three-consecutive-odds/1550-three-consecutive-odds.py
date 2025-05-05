class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 1
        for i in range(1,len(arr)):
            if arr[i]%2==1 and arr[i-1]%2==1:
                count+=1
            else:
                count = 1

            if count==3:
                return True
        return False