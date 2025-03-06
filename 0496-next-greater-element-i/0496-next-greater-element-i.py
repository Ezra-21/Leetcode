class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashh = {val:i for i,val in enumerate(nums1)}
        ans = [-1]*(len(nums1))
        stack = []
        for val in nums2:
            while stack and stack[-1]<val:
                num = stack.pop()
                idx = hashh[num]
                ans[idx] = val
            if val in hashh:
                stack.append(val)

        return ans


