class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)-1
        stack = []
        ans = [0]*len(temperatures)
        for i,val in enumerate(temperatures[::-1]):
            count = 0
            while stack and stack[-1][0]<=val:
                count+=ans[stack[-1][1]]
                stack.pop()

            if stack and stack[-1][0]>val:
                ans[n-i] = count+1

            stack.append([val,n-i])

        return ans
