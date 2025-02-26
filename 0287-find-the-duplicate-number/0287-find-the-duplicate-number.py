class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        i=0
        while i<len(arr):
            if arr[i]!=i+1:
                correct = arr[i]-1
                if arr[i]!=arr[correct]:
                    arr[i],arr[correct] = arr[correct],arr[i]
                else:
                    return arr[i]
            else:
                i+=1
        