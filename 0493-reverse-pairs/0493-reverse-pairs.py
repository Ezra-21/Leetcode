class Solution:
    def merge_sort(self,nums,l,r):
        if l>=r:
            return 0
        count = 0
        mid = (l+r)//2
        count+=self.merge_sort(nums,l,mid)
        count+=self.merge_sort(nums,mid+1,r)
        count+=self.merge(nums,l,mid,r)

        return count

    def merge(self,nums,l,mid,r):
        j = mid + 1  
        count = 0

        for i in range(l, mid + 1):
            while j <= r and nums[i] > 2 * nums[j]:
                j += 1
            count += (j - (mid + 1))
            
        i,j = l,mid+1
        temp = []
        while i<=mid and j<=r:
            if nums[i]<=nums[j]:
                temp.append(nums[i])
                i+=1
            else:
                
                temp.append(nums[j])
                j+=1
        temp.extend(nums[i:mid+1])
        temp.extend(nums[j:r+1])
        for i in range(len(temp)):
            nums[l+i] = temp[i]

        return count


        
    def reversePairs(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        return self.merge_sort(nums,l,r)

        
        
