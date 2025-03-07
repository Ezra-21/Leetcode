class Solution:
    def maxWidthRamp(self, num: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(num)):
            if not stack or num[stack[-1]]>num[i]:
                stack.append(i)
            elif num[stack[-1]] <= num[i]:
                ans = max(ans,i-stack[-1])

        i = len(num)-1
        while i>=0:
            if stack and num[stack[-1]] <= num[i]:
                ans = max(ans,i-stack[-1])
                stack.pop()
            else:
                i-=1

        return ans
            

