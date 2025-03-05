class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n,m = len(nums1),len(nums2)
        
        ans = []
        for i in range(n):
            flag = True
            j = 0
            while j<m:
                if nums1[i]==nums2[j]:
                    j+=1
                    while j<m:
                        if nums2[j]>nums1[i]:
                            ans.append(nums2[j])
                            flag = False
                            break
                        j+=1
                    break
                j+=1
            if flag:
                ans.append(-1)

        return ans


