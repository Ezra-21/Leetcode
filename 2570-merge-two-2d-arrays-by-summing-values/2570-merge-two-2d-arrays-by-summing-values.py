class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        ans = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i][0] == nums2[j][0]:
                ans.append([nums1[i][0],nums1[i][1]+nums2[j][1]])
                i+=1
                j+=1
            elif nums1[i][0] < nums2[j][0]:
                ans.append([nums1[i][0],nums1[i][1]])
                i+=1
            else:
                ans.append([nums2[j][0],nums2[j][1]])
                j+=1
        ans.extend(nums1[i:])
        ans.extend(nums2[j:])

        return ans



        