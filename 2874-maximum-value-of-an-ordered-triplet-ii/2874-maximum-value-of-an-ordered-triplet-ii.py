class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        # Precompute max_right array
        max_right = [0] * n
        max_right[-1] = nums[-1]
        for k in range(n-2, -1, -1):
            max_right[k] = max(max_right[k+1], nums[k])
        
        # Compute max_diff array using a monotonic stack
        max_diff = [0] * n
        stack = []
        for j in range(n):
            while stack and nums[stack[-1]] < nums[j]:
                stack.pop()
            if stack:
                max_diff[j] = nums[stack[0]] - nums[j]
            else:
                max_diff[j] = 0
            if not stack or nums[j] > nums[stack[0]]:
                stack.append(j)
        
        # Calculate the maximum triplet value
        res = 0
        for j in range(n-1):
            res = max(res, max_diff[j] * max_right[j+1])
        
        return res