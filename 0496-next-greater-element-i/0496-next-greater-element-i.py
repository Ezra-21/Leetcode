class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        dic = {val:i for i,val in enumerate(nums1)}
        ans = [-1]*n
        stack = []
        for val in nums2:
            while stack and stack[-1]<val:
                idx = dic[stack.pop()]
                ans[idx] = val
            if val in dic:
                stack.append(val)
        return ans