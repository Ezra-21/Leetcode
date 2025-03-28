class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,start,mid,end):
            left , right = start , mid+1
            lis = []
            while left<=mid and right<=end:
                if arr[left]<=arr[right]:
                    lis.append(arr[left])
                    left+=1
                else:
                    lis.append(arr[right])
                    right+=1
            lis.extend(arr[left:mid+1])
            lis.extend(arr[right:end+1])
            for i in range(len(lis)):
                arr[start+i]=lis[i]
            return arr

            
        def mergesort(arr,start,end):
            if len(arr)==1:
                return arr
            
            if start<end:
                mid = (start+end)//2
                mergesort(arr,start,mid)
                mergesort(arr,mid+1,end)
                merge(arr,start,mid,end)
            return arr

        start,end = 0,len(nums)-1
        return mergesort(nums,start,end)