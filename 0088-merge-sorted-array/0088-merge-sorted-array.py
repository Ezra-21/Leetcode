class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        right1,right2 = m-1,n-1
        n = len(nums1)-1

        while right1>=0 and right2>=0:
            if nums2[right2] > nums1[right1]:
                nums1[n] = nums2[right2]
                right2-=1
            else:
                nums1[n] = nums1[right1]
                right1-=1

            n-=1

        while right2>=0:
            nums1[n] = nums2[right2]
            right2-=1
            n-=1
            
        
        







        