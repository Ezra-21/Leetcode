class Solution:
    def findDisappearedNumbers(self, arr: List[int]) -> List[int]:
        lis = []
        i=0
        while i<len(arr):
            correct = arr[i]-1
            if correct<len(arr) and arr[i]!=arr[correct]:
                arr[i],arr[correct] = arr[correct],arr[i]
            else:
                i+=1
        for i in range(len(arr)):
            if i!=arr[i]-1:
                lis.append(i+1)
        return lis
        